# Instagram Unlike Reels Script

This script allows you to automatically unlike Instagram reels that you've previously liked. It fetches your liked reels and processes them in batches to unlike them efficiently.

## ⚠️ Important Disclaimer

This script is for educational purposes only. Use at your own risk and in compliance with Instagram's Terms of Service. Excessive automation may result in account restrictions.

## Prerequisites

- Python 3.7+
- Active Instagram account
- Modern web browser (Chrome, Firefox, Safari, Edge)

## Installation

1. Clone or download this repository
2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Setup Instructions

### Step 1: Get Fresh Session Data from Browser

You need to extract session data from your active Instagram web session. Follow these steps:

#### 1.1 Open Instagram in Browser
- Open your web browser
- Go to [Instagram.com](https://www.instagram.com)
- Log in to your account
- Navigate to your activity page: `https://www.instagram.com/your_activity/interactions/likes`

#### 1.2 Open Developer Tools
- Press `F12` or right-click and select "Inspect"
- Go to the **Network** tab
- Make sure "Preserve log" is checked

#### 1.3 Trigger a Like/Unlike Action
- On the likes page, find a reel you've liked
- Click the unlike button (heart icon)
- Look for the network request in the Developer Tools

#### 1.4 Extract Cookies
In the **Application** tab (Chrome) or **Storage** tab (Firefox):
1. Click on **Cookies** → **https://www.instagram.com**
2. Copy these cookie values:
   - `datr`
   - `ig_did`
   - `ig_nrcb`
   - `ps_l`
   - `ps_n`
   - `mid`
   - `csrftoken`
   - `ds_user_id`
   - `sessionid`
   - `wd`
   - `rur`

#### 1.5 Extract Headers
From the network request you captured:
1. Find the request to `async/wbloks/fetch/`
2. Copy these headers:
   - `User-Agent`
   - `Accept`
   - `Accept-Language`
   - `Content-Type`
   - `Origin`
   - `Referer`
   - `Sec-Fetch-Site`
   - `Sec-Fetch-Mode`
   - `Sec-Fetch-Dest`

#### 1.6 Extract BKV Value
1. In the network request, look for the `__bkv` parameter
2. Copy the value (it's a long string of letters and numbers)

#### 1.7 Extract Form Data
From the same network request, copy these form data values:
- `__d`
- `__user`
- `__a`
- `__req`
- `__hs`
- `dpr`
- `__ccg`
- `__rev`
- `__s`
- `__hsi`
- `__dyn`
- `__csr`
- `__hsdp`
- `__hblp`
- `__sjsp`
- `__comet_req`
- `fb_dtsg`
- `jazoest`
- `lsd`
- `__spin_r`
- `__spin_b`
- `__spin_t`
- `__crn`

### Step 2: Update the Script

Replace the values in the script with your extracted data:

```python
# Update these values with your session data
COOKIES = {
    "datr": "YOUR_DATR_VALUE",
    "ig_did": "YOUR_IG_DID_VALUE",
    "ig_nrcb": "YOUR_IG_NRCB_VALUE",
    "ps_l": "YOUR_PS_L_VALUE",
    "ps_n": "YOUR_PS_N_VALUE",
    "mid": "YOUR_MID_VALUE",
    "csrftoken": "YOUR_CSRFTOKEN_VALUE",
    "ds_user_id": "YOUR_DS_USER_ID_VALUE",
    "sessionid": "YOUR_SESSIONID_VALUE",
    "wd": "YOUR_WD_VALUE",
    "rur": "YOUR_RUR_VALUE"
}

headers = {
    "User-Agent": "YOUR_USER_AGENT",
    "Accept": "YOUR_ACCEPT_VALUE",
    "Accept-Language": "YOUR_ACCEPT_LANGUAGE",
    "Content-Type": "YOUR_CONTENT_TYPE",
    "Origin": "YOUR_ORIGIN",
    "Referer": "YOUR_REFERER",
    "Sec-Fetch-Site": "YOUR_SEC_FETCH_SITE",
    "Sec-Fetch-Mode": "YOUR_SEC_FETCH_MODE",
    "Sec-Fetch-Dest": "YOUR_SEC_FETCH_DEST"
}

BKV = "YOUR_BKV_VALUE"

DATA = {
    "__d": "YOUR_D_VALUE",
    "__user": "YOUR_USER_VALUE",
    "__a": "YOUR_A_VALUE",
    "__req": "YOUR_REQ_VALUE",
    "__hs": "YOUR_HS_VALUE",
    "dpr": "YOUR_DPR_VALUE",
    "__ccg": "YOUR_CCG_VALUE",
    "__rev": "YOUR_REV_VALUE",
    "__s": "YOUR_S_VALUE",
    "__hsi": "YOUR_HSI_VALUE",
    "__dyn": "YOUR_DYN_VALUE",
    "__csr": "YOUR_CSR_VALUE",
    "__hsdp": "YOUR_HSDP_VALUE",
    "__hblp": "YOUR_HBLP_VALUE",
    "__sjsp": "YOUR_SJSP_VALUE",
    "__comet_req": "YOUR_COMET_REQ_VALUE",
    "fb_dtsg": "YOUR_FB_DTSG_VALUE",
    "jazoest": "YOUR_JAZOEST_VALUE",
    "lsd": "YOUR_LSD_VALUE",
    "__spin_r": "YOUR_SPIN_R_VALUE",
    "__spin_b": "YOUR_SPIN_B_VALUE",
    "__spin_t": "YOUR_SPIN_T_VALUE",
    "__crn": "YOUR_CRN_VALUE",
    "params": "{}"
}
```

## Usage

### Basic Usage
```bash
python unlike_insta_reels_script.py
```

### Testing the API First
Uncomment the test function in the script to verify your session data:
```python
# Uncomment this line to test the unlike API first
test_unlike_api()
```

## How It Works

1. **Fetch Liked Reels**: The script fetches your liked reels using Instagram's internal API
2. **Extract Media IDs**: It parses the response to extract media IDs of liked reels
3. **Batch Processing**: Processes reels in batches of 100 to avoid overwhelming the API
4. **Unlike Requests**: Sends unlike requests for each batch
5. **Error Handling**: Includes session validation and error recovery

## Features

- ✅ Batch processing (100 reels at a time)
- ✅ Session validation and error handling
- ✅ Dynamic value extraction from responses
- ✅ Progress tracking
- ✅ Rate limiting to avoid detection
- ✅ Detailed logging and debugging

## Troubleshooting

### Session Expired Error
If you see error `1357004`, your session has expired:
1. Close and reopen your browser
2. Log out and log back into Instagram
3. Get fresh cookies and form data
4. Update the script with new values

### 500 Server Error
If you get a 500 error:
1. Check that all form data values are correct
2. Ensure cookies are fresh and valid
3. Try with a smaller batch size

### No Reels Found
If no reels are found:
1. Verify you have liked reels in your account
2. Check that the session is valid
3. Ensure you're on the correct activity page

## Security Notes

- Never share your session data (cookies, tokens) publicly
- Session data expires regularly - update when needed
- Use this script responsibly and in moderation
- Consider Instagram's rate limits and terms of service

## File Structure

```
insta/
├── unlike_insta_reels_script.py  # Main script
├── requirements.txt               # Python dependencies
└── README.md                     # This file
```

## Dependencies

- `requests`: HTTP library for API calls
- `json`: JSON parsing
- `time`: Rate limiting and delays
- `copy`: Deep copying of data structures

## Contributing

Feel free to submit issues and enhancement requests. Please ensure any changes maintain the script's safety and compliance with Instagram's terms.

## License

This project is for educational purposes. Use responsibly and in compliance with all applicable terms of service. 