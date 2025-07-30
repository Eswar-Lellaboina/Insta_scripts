import requests
import json
import time
from copy import deepcopy

# Replace with your actual values
COOKIES = {
            "datr": "19xFaOH3hH4lwyF7W-9RShUQ",
            "ig_did": "64DD6029-DEA6-4D86-937B-BA182AA70BFB",
            "ig_nrcb": "1",
            "ps_l": "1",
            "ps_n": "1",
            "mid": "aHS4CQAEAAHWezkFdSS-THqFYX9H",
            "csrftoken": "k60b3lj8UU3WHkv6BiAGuDgN1lRtFVWr",
            "ds_user_id": "21672007329",
            "sessionid": "21672007329%3AdAucCKfNjCH9dt%3A26%3AAYdb_9gl83J0q2-ADmqHh33-ccoy_maQYbL6lEG4ng",
            "wd": "1240x517",
            "rur": "HIL\05421672007329\0541785070089:01fe5a35277fe8b41fae071af348e974e6531c87466777441f8769e365befac28d56bab4"
            }

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9,te;q=0.8",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://www.instagram.com",
    "Referer": "https://www.instagram.com/your_activity/interactions/likes",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty"
}

BKV = "e1456a3f58800541d8a2ea65b55937920007fee744eed6e5b1a7723cbe417e5f"

DATA = {
    "__d": "www",
    "__user": "0",
    "__a": "1",
    "__req": "24",
    "__hs": "20295.HYP:instagram_web_pkg.2.1...0",
    "dpr": "2",
    "__ccg": "EXCELLENT",
    "__rev": "1025186088",
    "__s": "1vm5ty:s9bpuo:72z30c",
    "__hsi": "7531371530547075969",
    "__dyn": "7xeUjG1mxu1syUbFp41twWwIxu13wvoKewSAwHwNw9G2S7o2vwpUe8hw2nVE4W0qa0FE2awgo9oO0n24oaEnxO1ywOwv89k2C1Fwc60AEC1TwQzXwae4UaEW2G0AEco5G1Wxfxm16wUwtE1wEbUGdG1QwTU9UaQ0z8c86-3u2WE5B08-269wr86C1mgcEed6goK2O4Xxui2qi7E5y4UrwHwGwgU5SbBK4o11olxO7EG3a13Aw",
    "__csr": "g9YLb7R1daBtn3BOW9WTd94EG8yPNdQSCVK-DcBR_UxvBWFrGmAFaahp5VKmVAnWAqQ9biuKlFkKcDChWKHV9ejBXWswyFAVfBVoWiFAjFe9BK9hA6-m2m2qEXHmKjDDybgkal7ADiQi4pqxfAigmxbp4ex6VoKhG6opG4Ey4oqKiaxy59Umx200lOK9pA0kta4A0rlwglx-0OU3WwdGpwdO1_woE2hnOw1NeU0VN7UgAwzg8Ot6kg0uq3G8gGgw1eA34gawpA1UyoK0TolO06BEM6hk6Q0pC4Ulw4IgK0ry00yFE1NU1kE0bM8",
    "__hsdp": "gc7axzf6P9MD5hV1dqF430qujazi9PYIG1gCiAFpQymK8et8ZF0mnAS8kNNiovDzMQOp5UR4XNgig9y22akFq8L1km8Cod9K7F8n82abCp6mh4y45Ery-5UuwEQUfk3gU-byomUf478S2W69Eqyo5K9w7nK0j5059wuo1s82RwoE5O3e1swzxq2y0Ao7i0IEdo2XgaU2tc0i22Na214xTgO1Gw810tUb8S",
    "__hblp": "0PwTx22WbwGyovzKjgGU9u5Rz8lK0zohAwvFogAKazGCgpBzpomwHgN2VEa4mu6bghGi2h1m9KLVEnyJ7By5Wx2VomUade8x22m17UyHCzpSq22547byozU-4qKqahk6oxam10xK4e0Q8rwoUC1FKi0-8hwxg5K3S0HU7CawNw4Pw9-5o6aq3a2a7VaBBwiEW2SfwEw96i1Lwpo4O3m0BU8Q22axm2C1tcq0QU4m2NaESfh8tQEC9K1sxd0Hw-u2m5oK2S2OdG",
    "__sjsp": "gc7axz9krcCwB5hV1dqF430qujazi9PYIG3QiCtamt2qUmgzAg5DV8Se50ADzMQOp4UWjL5190C888FiByf1k5Ue-7E5lwwgfK1yK0yo1pU",
    "__comet_req": "7",
    "fb_dtsg": "NAfvseN3-lib1KRYSm9cwMH6vYsTPuXQ2t8qX-45pxIjEzzJGqtpXHA:17854231342124680:1753534075",
    "jazoest": "26322",
    "lsd": "0dnzb84QVFNPXnnW2Wmr18",
    "__spin_r": "1025186088",
    "__spin_b": "trunk",
    "__spin_t": "1753534081",
    "__crn": "comet.igweb.PolarisYourActivityInteractionsRoute",
    "params": "{}"
    }

# End of Replacable value from session

FETCH_LIKED_REELS_URL = "https://www.instagram.com/async/wbloks/fetch/"
UNLIKE_REELS_URL = "https://www.instagram.com/async/wbloks/fetch/"

def fetch_liked_reels(after_cursor=None):
    url = "https://www.instagram.com/async/wbloks/fetch/"
    params = {
        "appid": "com.instagram.privacy.activity_center.liked_media_screen",
        "type": "app",
        "__bkv": BKV
    }

    response = requests.post(url, headers=headers, cookies=COOKIES, params=params, data=DATA)

    if response.status_code == 200:
        print("Success!")
        try:
            # Parse the response - it starts with "for (;;);" followed by JSON
            response_text = response.text
            if response_text.startswith("for (;;);"):
                json_str = response_text[9:]  # Remove "for (;;);" prefix
                data = json.loads(json_str)
            else:
                data = response.json()
            
            # Extract media IDs from the complex UI structure
            reels = []
            
            # The response contains media data in a complex nested structure
            # We need to extract media_id_user_id pairs from the UI components
            response_str = json.dumps(data)
            
            # Look for media_id patterns in the response
            import re
            
            # Based on the debug output, media IDs are in the format:
            # (bk.action.array.Make, "3679495473192189417_64817826143", "DMQMaNYRz3p", "clips", ...
            # So we need to find patterns like: "number_number" where number is 15+ digits
            
            # Try different patterns to find media IDs
            print("🔍 Trying different media ID patterns...")
            
            patterns_to_try = [
                r'"([0-9]{15,}_[0-9]+)"',  # Long numbers with underscore in quotes
                r'\b([0-9]{15,}_[0-9]+)\b', # Long numbers with underscore, word boundaries
                r'"([0-9]{10,}_[0-9]+)"',   # Medium numbers with underscore in quotes
                r'\b([0-9]{10,}_[0-9]+)\b', # Medium numbers with underscore, word boundaries
                r'"([0-9]+_[0-9]+)"',        # Any numbers with underscore in quotes
                r'\b([0-9]+_[0-9]+)\b',      # Any numbers with underscore, word boundaries
            ]
            
            media_matches = []
            for i, pattern in enumerate(patterns_to_try):
                matches = re.findall(pattern, response_str)
                print(f"Pattern {i+1}: {pattern}")
                print(f"  Found {len(matches)} matches: {matches[:5]}...")
                if matches:
                    media_matches = matches
                    break
            
            print(f"🔍 Using pattern {i+1}, found {len(media_matches)} potential media IDs: {media_matches[:10]}...")
            
            # Also search for very long numbers (15+ digits) that might be media IDs
            long_numbers = re.findall(r'([0-9]{15,})', response_str)
            print(f"🔍 Found {len(long_numbers)} long numbers (15+ digits): {long_numbers[:10]}...")
            
            # Search for the specific pattern you mentioned
            specific_pattern = re.findall(r'([0-9]{19}_[0-9]{11})', response_str)
            print(f"🔍 Found {len(specific_pattern)} matches for 19-digit_11-digit pattern: {specific_pattern[:5]}...")
            
            # Filter out UI component IDs and file/asset IDs, keep only media IDs
            # Media IDs are typically 15+ digits followed by underscore and more digits
            filtered_matches = []
            for match in media_matches:
                # Skip UI component IDs (shorter numbers)
                if len(match.split('_')[0]) < 15:
                    print(f"❌ Filtering out UI component ID: {match}")
                    continue
                
                # Skip file/asset IDs (numbers with _n suffix)
                if match.endswith('_n'):
                    print(f"❌ Filtering out file/asset ID: {match}")
                    continue
                
                # Skip IDs with too many underscores (likely file paths)
                if match.count('_') > 1:
                    print(f"❌ Filtering out multi-underscore ID: {match}")
                    continue
                
                # Additional check: ensure the match is not part of a larger string with _n suffix
                # Look for the pattern in the original response to see if it's part of a larger string
                import re
                # Check if this match is followed by _n in the original response
                pattern_with_n = re.escape(match) + r'_n'
                if re.search(pattern_with_n, response_str):
                    print(f"❌ Filtering out ID that's part of larger _n pattern: {match}")
                    continue
                
                # Additional validation: ensure both parts are reasonable lengths
                parts = match.split('_')
                if len(parts) != 2:
                    print(f"❌ Filtering out invalid format: {match}")
                    continue
                
                # First part should be 15+ digits, second part should be reasonable length
                if len(parts[0]) < 15 or len(parts[1]) < 5:
                    print(f"❌ Filtering out ID with invalid part lengths: {match}")
                    continue
                
                filtered_matches.append(match)
                print(f"✅ Keeping media ID: {match}")
            
            media_matches = filtered_matches
            print(f"🔍 After filtering: {len(media_matches)} media IDs")
            
            for media_id in media_matches:
                if media_id not in reels:  # Avoid duplicates
                    reels.append(media_id)
            
            print(f"Found {len(reels)} liked media items")
            
            # Extract dynamic values for unlike requests
            dynamic_values = extract_dynamic_values(response_str)
            
            # For pagination, we'll need to implement cursor-based logic
            # The response doesn't seem to have clear pagination info in the sample
            next_cursor = None  # You may need to extract this from the response

            # Debug: Print a sample of the response to see the structure
            # print("🔍 Response structure sample:")
            # print(response_str[:2000])  # Print first 2000 chars

            return reels, next_cursor, dynamic_values

        except Exception as e:
            print("Error parsing reels:", e)
            print("Response structure:", response.text[:500])  # Print first 500 chars for debugging
            return [], None, {}
    else:
        print(f"Failed with status {response.status_code}")
        print(response.text)
        return [], None, {}

def extract_dynamic_values(response_str):
    """Extract dynamic values from the likes API response for unlike requests"""
    import re
    import urllib.parse
    
    dynamic_values = {}
    
    print("🔍 Searching for dynamic values in response...")
    print(f"Response length: {len(response_str)} characters")
    
    # Look for the activity_center_params field which contains the dynamic values
    activity_params_pattern = r'"activity_center_params","([^"]+)"'
    activity_params_match = re.search(activity_params_pattern, response_str)
    
    if activity_params_match:
        params_str = activity_params_match.group(1)
        print(f"✅ Found activity_center_params: {params_str[:100]}...")
        
        # URL decode the params
        try:
            decoded_params = urllib.parse.unquote(params_str)
            print(f"✅ Decoded activity_center_params: {decoded_params[:200]}...")
            
            # Parse the JSON in params
            params_data = json.loads(decoded_params)
            
            # Extract the dynamic values from params
            if 'content_container_id' in params_data:
                dynamic_values['content_container_id'] = params_data['content_container_id']
                print(f"✅ Found content_container_id: {params_data['content_container_id']}")
            
            if 'content_element_id' in params_data:
                dynamic_values['content_element_id'] = params_data['content_element_id']
                print(f"✅ Found content_element_id: {params_data['content_element_id']}")
            
            if 'content_spinner_id' in params_data:
                dynamic_values['content_spinner_id'] = params_data['content_spinner_id']
                print(f"✅ Found content_spinner_id: {params_data['content_spinner_id']}")
                
        except Exception as e:
            print(f"❌ Error parsing activity_center_params: {e}")
    
    # Look for unlike-specific container IDs in the response
    # These might be in a different format or location than the likes container IDs
    print("🔍 Searching for unlike-specific container IDs...")
    
    # Look for patterns that might contain unlike container IDs
    unlike_container_patterns = [
        r'"unlike_container_id":(\d+)',
        r'unlike_container_id["\s]*:["\s]*(\d+)',
        r'"unlike_content_container_id":(\d+)',
        r'unlike_content_container_id["\s]*:["\s]*(\d+)',
        r'"action_container_id":(\d+)',
        r'action_container_id["\s]*:["\s]*(\d+)',
        # Look for any large numbers that might be unlike container IDs
        r'(\d{8,})',  # 8+ digit numbers
    ]
    
    unlike_container_ids = []
    for pattern in unlike_container_patterns:
        matches = re.findall(pattern, response_str)
        if matches:
            print(f"🔍 Found potential unlike container IDs with pattern {pattern}: {matches[:5]}")
            unlike_container_ids.extend([int(match) for match in matches])
    
    # If we found potential unlike container IDs, use them
    if unlike_container_ids:
        # Remove duplicates and ensure we have different values
        unique_container_ids = list(dict.fromkeys(unlike_container_ids))  # Remove duplicates while preserving order
        
        if len(unique_container_ids) >= 3:
            # We have enough unique container IDs
            dynamic_values['unlike_content_container_id'] = unique_container_ids[0]
            dynamic_values['unlike_content_element_id'] = unique_container_ids[1]
            dynamic_values['unlike_content_spinner_id'] = unique_container_ids[2]
            print(f"✅ Found unique unlike container IDs: {unique_container_ids[:3]}")
        elif len(unique_container_ids) >= 1:
            # We have at least one unique ID, generate sequential ones
            base_id = unique_container_ids[0]
            dynamic_values['unlike_content_container_id'] = base_id
            dynamic_values['unlike_content_element_id'] = base_id + 1
            dynamic_values['unlike_content_spinner_id'] = base_id + 2
            print(f"✅ Generated sequential unlike container IDs from base {base_id}: {base_id}, {base_id+1}, {base_id+2}")
        else:
            print("⚠️ No valid unlike container IDs found")
    else:
        print("⚠️ No unlike container IDs found in response")
    
    # If we didn't find activity_center_params, look for the values directly in the response
    if not dynamic_values.get('content_container_id'):
        container_patterns = [
            r'"content_container_id":(\d+)',
            r'content_container_id["\s]*:["\s]*(\d+)',
            r'container_id["\s]*:["\s]*(\d+)'
        ]
        
        for pattern in container_patterns:
            container_match = re.search(pattern, response_str)
            if container_match:
                dynamic_values['content_container_id'] = int(container_match.group(1))
                print(f"✅ Found content_container_id: {container_match.group(1)}")
                break
    
    if not dynamic_values.get('content_element_id'):
        element_patterns = [
            r'"content_element_id":(\d+)',
            r'content_element_id["\s]*:["\s]*(\d+)',
            r'element_id["\s]*:["\s]*(\d+)'
        ]
        
        for pattern in element_patterns:
            element_match = re.search(pattern, response_str)
            if element_match:
                dynamic_values['content_element_id'] = int(element_match.group(1))
                print(f"✅ Found content_element_id: {element_match.group(1)}")
                break
    
    if not dynamic_values.get('content_spinner_id'):
        spinner_patterns = [
            r'"content_spinner_id":(\d+)',
            r'content_spinner_id["\s]*:["\s]*(\d+)',
            r'spinner_id["\s]*:["\s]*(\d+)'
        ]
        
        for pattern in spinner_patterns:
            spinner_match = re.search(pattern, response_str)
            if spinner_match:
                dynamic_values['content_spinner_id'] = int(spinner_match.group(1))
                print(f"✅ Found content_spinner_id: {spinner_match.group(1)}")
                break
    
    # Extract session tokens from the response
    fb_dtsg_patterns = [
        r'"fb_dtsg":"([^"]+)"',
        r'fb_dtsg["\s]*:["\s]*([^"]+)',
        r'fb_dtsg["\s]*:["\s]*([^"]+)'
    ]
    
    for pattern in fb_dtsg_patterns:
        fb_dtsg_match = re.search(pattern, response_str)
        if fb_dtsg_match:
            dynamic_values['fb_dtsg'] = fb_dtsg_match.group(1)
            print(f"✅ Found fb_dtsg: {fb_dtsg_match.group(1)[:20]}...")
            break
    
    jazoest_patterns = [
        r'"jazoest":"([^"]+)"',
        r'jazoest["\s]*:["\s]*([^"]+)',
        r'jazoest["\s]*:["\s]*([^"]+)'
    ]
    
    for pattern in jazoest_patterns:
        jazoest_match = re.search(pattern, response_str)
        if jazoest_match:
            dynamic_values['jazoest'] = jazoest_match.group(1)
            print(f"✅ Found jazoest: {jazoest_match.group(1)}")
            break
    
    lsd_patterns = [
        r'"lsd":"([^"]+)"',
        r'lsd["\s]*:["\s]*([^"]+)',
        r'lsd["\s]*:["\s]*([^"]+)'
    ]
    
    for pattern in lsd_patterns:
        lsd_match = re.search(pattern, response_str)
        if lsd_match:
            dynamic_values['lsd'] = lsd_match.group(1)
            print(f"✅ Found lsd: {lsd_match.group(1)}")
            break
    
    # Extract request counters - use the values from the working unlike payload
    dynamic_values['__req'] = '28'  # From working unlike payload
    dynamic_values['__s'] = 'x972f9:s9bpuo:72z30c'  # From working unlike payload
    
    # Extract critical dynamic values that should be dynamic
    hsi_patterns = [
        r'"__hsi":"([^"]+)"',
        r'__hsi["\s]*:["\s]*([^"]+)',
        r'__hsi["\s]*:["\s]*([^"]+)'
    ]
    
    for pattern in hsi_patterns:
        hsi_match = re.search(pattern, response_str)
        if hsi_match:
            dynamic_values['__hsi'] = hsi_match.group(1)
            print(f"✅ Found __hsi: {hsi_match.group(1)}")
            break
    
    spin_t_patterns = [
        r'"__spin_t":"([^"]+)"',
        r'__spin_t["\s]*:["\s]*([^"]+)',
        r'__spin_t["\s]*:["\s]*([^"]+)'
    ]
    
    for pattern in spin_t_patterns:
        spin_t_match = re.search(pattern, response_str)
        if spin_t_match:
            dynamic_values['__spin_t'] = spin_t_match.group(1)
            print(f"✅ Found __spin_t: {spin_t_match.group(1)}")
            break
    
    # Extract critical dynamic parameters that should be dynamic
    dyn_patterns = [
        r'"__dyn":"([^"]+)"',
        r'__dyn["\s]*:["\s]*([^"]+)',
        r'__dyn["\s]*:["\s]*([^"]+)'
    ]
    
    for pattern in dyn_patterns:
        dyn_match = re.search(pattern, response_str)
        if dyn_match:
            dynamic_values['__dyn'] = dyn_match.group(1)
            print(f"✅ Found __dyn: {dyn_match.group(1)[:50]}...")
            break
    
    csr_patterns = [
        r'"__csr":"([^"]+)"',
        r'__csr["\s]*:["\s]*([^"]+)',
        r'__csr["\s]*:["\s]*([^"]+)'
    ]
    
    for pattern in csr_patterns:
        csr_match = re.search(pattern, response_str)
        if csr_match:
            dynamic_values['__csr'] = csr_match.group(1)
            print(f"✅ Found __csr: {csr_match.group(1)[:50]}...")
            break
    
    hsdp_patterns = [
        r'"__hsdp":"([^"]+)"',
        r'__hsdp["\s]*:["\s]*([^"]+)',
        r'__hsdp["\s]*:["\s]*([^"]+)'
    ]
    
    for pattern in hsdp_patterns:
        hsdp_match = re.search(pattern, response_str)
        if hsdp_match:
            dynamic_values['__hsdp'] = hsdp_match.group(1)
            print(f"✅ Found __hsdp: {hsdp_match.group(1)[:50]}...")
            break
    
    hblp_patterns = [
        r'"__hblp":"([^"]+)"',
        r'__hblp["\s]*:["\s]*([^"]+)',
        r'__hblp["\s]*:["\s]*([^"]+)'
    ]
    
    for pattern in hblp_patterns:
        hblp_match = re.search(pattern, response_str)
        if hblp_match:
            dynamic_values['__hblp'] = hblp_match.group(1)
            print(f"✅ Found __hblp: {hblp_match.group(1)[:50]}...")
            break
    
    sjsp_patterns = [
        r'"__sjsp":"([^"]+)"',
        r'__sjsp["\s]*:["\s]*([^"]+)',
        r'__sjsp["\s]*:["\s]*([^"]+)'
    ]
    
    for pattern in sjsp_patterns:
        sjsp_match = re.search(pattern, response_str)
        if sjsp_match:
            dynamic_values['__sjsp'] = sjsp_match.group(1)
            print(f"✅ Found __sjsp: {sjsp_match.group(1)[:50]}...")
            break
    
    # If we still don't find values, let's look for any numeric IDs that might be container IDs
    if not dynamic_values.get('content_container_id'):
        # Look for any large numbers that might be container IDs
        all_numbers = re.findall(r'(\d{8,})', response_str)
        if all_numbers:
            # Use the first large number as container_id
            dynamic_values['content_container_id'] = int(all_numbers[0])
            dynamic_values['content_element_id'] = int(all_numbers[0]) + 1
            dynamic_values['content_spinner_id'] = int(all_numbers[0]) + 2
            print(f"⚠️ Using fallback container IDs: {all_numbers[0]}, {int(all_numbers[0])+1}, {int(all_numbers[0])+2}")
    
    # Always ensure we have the minimum required values
    if not dynamic_values.get('content_container_id') or dynamic_values.get('content_container_id') == 0:
        print("❌ No valid container ID found, using hardcoded values")
        dynamic_values['content_container_id'] = 133715365
        dynamic_values['content_element_id'] = 133715366
        dynamic_values['content_spinner_id'] = 133715367
    
    if not dynamic_values.get('fb_dtsg'):
        dynamic_values['fb_dtsg'] = 'NAfu7EgYKiJ6mo3UJRz9X94WmF83keRle4TaT6ZIKn_v_sEmgIupTfw:17843696212148243:1752916359'
    
    if not dynamic_values.get('jazoest'):
        dynamic_values['jazoest'] = '26307'
    
    if not dynamic_values.get('lsd'):
        dynamic_values['lsd'] = 'pPUbtk_hxlr8prPo88m1wD'
    
    print(f"🔍 Final extracted dynamic values: {dynamic_values}")
    
    return dynamic_values

def unlike_reels_batch(media_id_user_ids, dynamic_values=None):
    assert len(media_id_user_ids) <= 100
    
    # Use dynamically extracted unlike container IDs if available, otherwise fallback to working values
    print("🔧 Using dynamically extracted unlike container IDs")
    
    # Check if we have unlike-specific container IDs from the dynamic extraction
    if dynamic_values and dynamic_values.get('unlike_content_container_id'):
        # Validate that the container IDs are different (not all the same)
        container_id = dynamic_values['unlike_content_container_id']
        element_id = dynamic_values['unlike_content_element_id']
        spinner_id = dynamic_values['unlike_content_spinner_id']
        
        if container_id == element_id == spinner_id:
            print("⚠️ All unlike container IDs are the same, using fallback values")
            use_fallback = True
        else:
            use_fallback = False
            print(f"✅ Using dynamically extracted unlike container IDs: {container_id}, {element_id}, {spinner_id}")
    else:
        use_fallback = True
        print("⚠️ No unlike container IDs found, using fallback values")
    
    if use_fallback:
        # Fallback to working values from unlike.txt
        print("🔧 Using fallback unlike container IDs from unlike.txt")
        unlike_dynamic_values = {
            'content_container_id': 1133615739,
            'content_element_id': 1133615740,
            'content_spinner_id': 1133615741,
            'fb_dtsg': dynamic_values.get('fb_dtsg', 'NAfvseN3-lib1KRYSm9cwMH6vYsTPuXQ2t8qX-45pxIjEzzJGqtpXHA:17854231342124680:1753534075'),
            'jazoest': dynamic_values.get('jazoest', '26322'),
            'lsd': dynamic_values.get('lsd', '0dnzb84QVFNPXnnW2Wmr18'),
            '__req': dynamic_values.get('__req', '24'),
            '__s': dynamic_values.get('__s', '1vm5ty:s9bpuo:72z30c'),
            '__hsi': dynamic_values.get('__hsi', '7531371530547075969'),
            '__spin_t': dynamic_values.get('__spin_t', '1753534081')
        }
    else:

        unlike_dynamic_values = {
            'content_container_id': container_id,
            'content_element_id': element_id,
            'content_spinner_id': spinner_id,
            'fb_dtsg': dynamic_values.get('fb_dtsg', 'NAfvseN3-lib1KRYSm9cwMH6vYsTPuXQ2t8qX-45pxIjEzzJGqtpXHA:17854231342124680:1753534075'),
            'jazoest': dynamic_values.get('jazoest', '26322'),
            'lsd': dynamic_values.get('lsd', '0dnzb84QVFNPXnnW2Wmr18'),
            '__req': dynamic_values.get('__req', '24'),
            '__s': dynamic_values.get('__s', '1vm5ty:s9bpuo:72z30c'),
            '__hsi': dynamic_values.get('__hsi', '7531371530547075969'),
            '__spin_t': dynamic_values.get('__spin_t', '1753534081')
        }
    
    # Extract media IDs from the batch
    media_ids = []
    for media_id in media_id_user_ids:
        # Handle both tuple format (media_id, user_id) and string format (media_id)
        if isinstance(media_id, tuple):
            media_id_str = media_id[0]  # Extract media_id from tuple
        else:
            media_id_str = media_id  # Use media_id directly if it's a string
        media_ids.append(media_id_str)
    
    # Join multiple media IDs with commas for batch unlike
    items_for_action = ",".join(media_ids)
    number_of_items = len(media_ids)
    
    # Determine if this is a single or multiple item request
    is_multiple = number_of_items > 1
    
    # Adjust request parameters based on number of items
    if is_multiple:
        # For multiple items, use '1n' instead of '1h' and different session identifier
        req_value = '1n'
        s_value = unlike_dynamic_values.get('__s', 'vfewk6:2y0vjy:makc7g')  # Different session for multiple items
        print(f"📦 Processing {number_of_items} reels in batch...")
    else:
        # For single item, use original values
        req_value = unlike_dynamic_values.get('__req', '1h')
        s_value = unlike_dynamic_values.get('__s', 'vfewk6:2y0vjy:makc7g')
        print(f"📦 Processing 1 reel...")
    
    params = {
        "content_container_id": unlike_dynamic_values.get('content_container_id', 133715365),
        "content_element_id": unlike_dynamic_values.get('content_element_id', 133715366),
        "content_spinner_id": unlike_dynamic_values.get('content_spinner_id', 133715367),
        "main_order_state_value": True,
        "main_attribute_order_state_value": "newest_to_oldest",
        "main_date_start_state_value": -1,
        "main_date_end_state_value": -1,
        "main_authors_state_value": "",
        "main_filter_to_visible_on_facebook_value": False,
        "main_includes_location_value": False,
        "main_liked_privately_value": False,
        "main_content_type_value": 0,
        "main_content_types_value": "Posts, Reels",
        "main_account_history_events_state_value": "",
        "entrypoint": "",
        "shared_user_id": "",
        "main_filter_to_visible_from_facebook_value": False,
        "items_for_action": items_for_action,  # Multiple media IDs joined with commas
        "number_of_items": number_of_items
    }

    unlike_form_data = deepcopy(DATA)
    unlike_form_data["params"] = json.dumps(params)

    params = {
        "appid": "com.instagram.privacy.activity_center.liked_unlike",
        "type": "action",
        "__bkv": BKV
    }

    response = requests.post(UNLIKE_REELS_URL, headers=headers, cookies=COOKIES, data=unlike_form_data, params=params)

    # response = requests.post(UNLIKE_REELS_URL, headers=headers, cookies=COOKIES, data=form_data)
    if response.status_code == 200:
        # Check if the response contains an error
        if "error" in response.text and "1357004" in response.text:
            print("⚠️ Session error (1357004) - Your session has expired")
            print("💡 Please refresh your browser session and update the cookies")
            print("🔧 You may need to:")
            print("   1. Close and reopen your browser")
            print("   2. Log out and log back into Instagram")
            print("   3. Get fresh cookies from your browser")
            return False  # Indicate failure so we can stop processing
        else:
            if is_multiple:
                print(f"✅ Successfully unliked {number_of_items} reels in batch")
            else:
                print(f"✅ Unliked reel: {media_ids[0]}")
            return True
    else:
        print(f"❌ Failed to unlike {'reels' if is_multiple else 'reel'}: {response.status_code}")
        print(f"Response: {response.text[:500]}...")  # Show first 500 chars
        
        # If it's a 500 error, the dynamic values might be wrong
        if response.status_code == 500:
            print(f"⚠️ 500 error - dynamic values might be incorrect:")
            print(f"   Container ID: {unlike_dynamic_values.get('content_container_id')}")
            print(f"   fb_dtsg: {unlike_dynamic_values.get('fb_dtsg', '')[:20]}...")
            print(f"   jazoest: {unlike_dynamic_values.get('jazoest')}")
            print(f"   lsd: {unlike_dynamic_values.get('lsd')}")
            print(f"   __req: {req_value}")
            print(f"   __s: {s_value}")
            print(f"   Items: {items_for_action}")
        return False
    

def main():
    next_cursor = None
    total_unliked = 0
    dynamic_values = None  # Will be set from first API call
    
    while True:
        liked_reels, next_cursor, new_dynamic_values = fetch_liked_reels(after_cursor=next_cursor)

        if not liked_reels:
            print("🎉 No more liked reels.")
            break
        
        # Use dynamic values from the first successful API call
        if new_dynamic_values and dynamic_values is None:
            dynamic_values = new_dynamic_values
            print(f"🔧 Using extracted dynamic values: {dynamic_values}")
        
        if not liked_reels:
            print("🎉 No more liked reels.")
            break
        
        print(f"📦 Processing {len(liked_reels)} reels...")
        
        # Process in smaller batches to avoid overwhelming the API
        for i in range(0, len(liked_reels), 100):  # Process 10 at a time instead of 100
            batch = liked_reels[i:i + 100]
            success = unlike_reels_batch(batch, dynamic_values)
            if not success:
                print("🛑 Stopping due to session error. Please refresh your session and try again.")
                break
            total_unliked += len(batch)
            print(f"📊 Progress: {total_unliked} reels unliked so far")
            time.sleep(3)  # Longer delay between batches
        
        # if not next_cursor:
        #     break
    
    print(f"🎉 Script completed! Total reels unliked: {total_unliked}")

def test_unlike_api():
    """Test the unlike API with a single reel to verify it works"""
    print("🧪 Testing unlike API...")
    
    # Test with a single reel ID from your sample
    test_reel_id = "3679619405794749084_67286303110"  # From your unlike.txt sample
    
    # Use the exact values from your unlike.txt sample
    test_dynamic_values = {
        'content_container_id': 1225513150,
        'content_element_id': 1225513151,
        'content_spinner_id': 1225513152,
        'fb_dtsg': 'NAfsS3ZFnCIO0jc3OE1gtUrRvwiexXT_ws-KxU3wkAqcc_SVsabLrIw:17865145036029998:1753043255',
        'jazoest': '26512',
        'lsd': '6pehYvRyF0o4NEDpdcq4Pp',
        '__req': '1d',
        '__s': '8xlw39:s9bpuo:482ahc',
        '__hsi': '7531359609186744699',
        '__spin_t': '1753531305'
    }
    
    unlike_reels_batch([test_reel_id], test_dynamic_values)

def get_fresh_cookies_instructions():
    """Print instructions for getting fresh cookies"""
    print("🔧 To get fresh cookies from your browser:")
    print("1. Open Instagram in your browser")
    print("2. Open Developer Tools (F12)")
    print("3. Go to Application/Storage tab")
    print("4. Look for Cookies under the Instagram domain")
    print("5. Copy the following cookies:")
    print("   - datr")
    print("   - ig_did")
    print("   - csrftoken")
    print("   - ds_user_id")
    print("   - sessionid")
    print("   - rur")
    print("   - wd")
    print("6. Update the COOKIES dictionary in the script")
    print("7. Also get fresh form data from a successful unlike request")

if __name__ == "__main__":
    # Uncomment the line below to test the unlike API first
    # test_unlike_api()
    
    # Uncomment the line below to get cookie instructions
    # get_fresh_cookies_instructions()
    
    main()
