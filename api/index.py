import json
from urllib.parse import parse_qs

def handler(request):
    # Enable CORS headers in response
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json',
    }
    
    if request.method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }

    # Load marks data
    with open('q-vercel-python.json') as f:
        data = json.load(f)

    # Parse query params
    query_params = parse_qs(request.query_string)
    names = query_params.get('name', [])

    marks = [data.get(name) for name in names]

    return {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps({'marks': marks})
    }
