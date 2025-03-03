import requests
from django.http import JsonResponse

def get_stock_data(request, symbol):
    try:
        api_key = 'cv2srqpr01qsrkiki6rgcv2srqpr01qsrkiki6s0'
        url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            return JsonResponse({'error': 'Impossible de récupérer les données'}, status=500)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)