from django.http import JsonResponse
import base64, json

def debug_claims(request):
    raw = request.META.get('X-MS-CLIENT-PRINCIPAL')
    if raw:
        decoded = base64.b64decode(raw).decode('utf-8')
        return JsonResponse(json.loads(decoded), safe=False)
    return JsonResponse({'error': 'No principal found'})


