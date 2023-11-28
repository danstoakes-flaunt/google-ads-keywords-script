#!/usr/bin/env python3

try:
    from google.ads.googleads.client import GoogleAdsClient
    client = GoogleAdsClient.load_from_storage("google-ads.yaml")
except ImportError as e:
    print("Some or all of the necessary packages to run the script are missing. Please consult the README for instructions on how to install them.")
    print(f"\nOriginal error: {e}")
    exit(1)