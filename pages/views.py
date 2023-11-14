from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def run_script(initial_href, ads_href, target_text, number_times):
    results = []

    # Append additional information to the results
    results.append(f"WEBSIT : {initial_href}")
    results.append(f"ADS : {ads_href}")
    results.append("---------------------------------------") 
    results.append(f"{number_times}")

    # Your provided script for LINK
    for _ in range(int(number_times)):
        response_link = requests.get(initial_href)

        if response_link.status_code == 200:
            soup_link = BeautifulSoup(response_link.text, 'html.parser')
            target_element = soup_link.find('a', string=lambda text: target_text in (text or ''))
            if target_element:
                initial_href = target_element.get('href')
                results.append(f"{initial_href}")
            else:
                results.append(f"\nRESULT\nTarget text '{target_text}' not found on the page.")
        else:
            results.append(f"\nRESULT\nFailed to retrieve the page. Status code: {response_link.status_code}")

    # Your provided script for ADS
    response_ads = requests.get(ads_href)
    results.append("---------------------------------------") 
    results.append("\nADS:")
    if response_ads.status_code == 200:
        soup_ads = BeautifulSoup(response_ads.text, 'html.parser')
        all_links_ads = soup_ads.find_all('a')

        # Extract and append the href attributes for ADS
        for link in all_links_ads:
            href = link.get('href')
            if href:
                results.append(f"{href}")
                results.append("")  # Add a space between ADS
    else:
        results.append(f"Failed to retrieve the ADS webpage. Status code: {response_ads.status_code}")

    return results

def about(request):
    if request.method == 'POST':
        initial_href = request.POST.get('initial_href')
        ads_href = request.POST.get('ads_href')
        target_text = request.POST.get('target_text')
        number_times = request.POST.get('number_times')

        # Run the combined script
        results = run_script(initial_href, ads_href, target_text, number_times)

        return render(request, 'pages/about.html', {'results': results})

    return render(request, 'pages/about.html')

def pagetow(request):
    return render(request, 'pages/about.html')
