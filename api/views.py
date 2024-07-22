from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
import json
from ytmusicapi import YTMusic

# Initialize YTMusic with authentication headers
ytmusic = YTMusic('headers_auth.json')

# Generic function to handle API responses
def handle_response(api_function, *args, **kwargs):
    try:
        response = api_function(*args, **kwargs)
        if response:
            return JsonResponse(response, safe=False, status=200)
        else:
            return JsonResponse({'message': 'No data found.'}, status=404)
    except Exception as e:
        print(f'Error: {e}')
        return JsonResponse({'message': 'Internal server error.'}, status=500)

@csrf_exempt
@require_POST
def search(request):
    data = json.loads(request.body)
    return handle_response(
        ytmusic.search,
        data.get('query', ''),
        data.get('filter', ''),
        scope=data.get('scope', None),
        limit=data.get('limit', 10),
        ignore_spelling=data.get('ignoreSpelling', True)
    )

@csrf_exempt
@require_POST
def suggestions(request):
    data = json.loads(request.body)
    return handle_response(
        ytmusic.get_search_suggestions,
        data.get('query', ''),
        data.get('detailed_runs', False)
    )

@csrf_exempt
@require_POST
def home(request):
    data = json.loads(request.body)
    return handle_response(ytmusic.get_home, limit=data.get('limit', 3))

@csrf_exempt
@require_POST
def artist(request):
    data = json.loads(request.body)
    return handle_response(ytmusic.get_artist, data.get('channelId', ''))

@csrf_exempt
@require_POST
def artist_albums(request):
    data = json.loads(request.body)
    return handle_response(
        ytmusic.get_artist_albums,
        data.get('channelId', ''),
        data.get('params', ''),
        limit=data.get('limit', 100),
        order=data.get('order', None)
    )

@csrf_exempt
@require_POST
def album(request):
    data = json.loads(request.body)
    return handle_response(ytmusic.get_album, data.get('browseId', ''))

@csrf_exempt
@require_POST
def album_browse_id(request):
    data = json.loads(request.body)
    return handle_response(ytmusic.get_album_browse_id, data.get('audioPlaylistId', ''))

@csrf_exempt
@require_POST
def user(request):
    data = json.loads(request.body)
    return handle_response(ytmusic.get_user, data.get('channelId', ''))

@csrf_exempt
@require_POST
def song_related(request):
    data = json.loads(request.body)
    return handle_response(ytmusic.get_song_related, data.get('browseId', ''))

@csrf_exempt
@require_POST
def lyrics(request):
    data = json.loads(request.body)
    return handle_response(ytmusic.get_lyrics, data.get('browseId', ''))

@require_GET
def tasteprofile(request):
    return handle_response(ytmusic.get_tasteprofile)

@require_GET
def mood_categories(request):
    return handle_response(ytmusic.get_mood_categories)

@csrf_exempt
@require_POST
def mood_playlists(request):
    data = json.loads(request.body)
    return handle_response(ytmusic.get_mood_playlists, data.get('params', ''))
