# Exchange rate data (Using provided JSON data)
exchange_rates = {
    "USD": 1, "AED": 3.6725, "AFN": 72.6525, "ALL": 91.477, "AMD": 394.4814,
    "ANG": 1.79, "AOA": 919.553, "ARS": 1066.04, "AUD": 1.5867, "AWG": 1.79,
    "AZN": 1.7002, "BAM": 1.8023, "BDT": 121.4947, "BGN": 1.8023, "BHD": 0.376,
    "BIF": 2964.4488, "BMD": 1, "BND": 1.3299, "BOB": 6.9166, "BRL": 5.7685,
    "BSD": 1, "BTN": 87.2198, "BWP": 13.655, "BYN": 3.2653, "BZD": 2, "CAD": 1.4368,
    "CDF": 2854.4436, "CHF": 0.8783, "CLP": 928.7979, "CNY": 7.2423, "COP": 4139.2719,
    "CRC": 504.0267, "CUP": 24, "CVE": 101.6112, "CZK": 23.0039, "DKK": 6.8742,
    "DOP": 62.1393, "DZD": 133.4164, "EGP": 50.6449, "ERN": 15, "EUR": 0.9215,
    "FJD": 2.2912, "GBP": 0.7735, "GHS": 15.5463, "HKD": 7.7711, "INR": 87.2201,
    "JPY": 147.6407, "KES": 129.1744, "KRW": 1445.8595, "MXN": 20.2757, "MYR": 4.415,
    "NOK": 10.8438, "NZD": 1.751, "PHP": 57.4498, "PKR": 280.0416, "PLN": 3.8408,
    "QAR": 3.64, "RON": 4.5856, "RUB": 89.7655, "SAR": 3.75, "SEK": 10.0793,
    "SGD": 1.3299, "THB": 33.6082, "TRY": 36.5318, "TWD": 32.7996, "UAH": 41.237,
    "UGX": 3670.1499, "USD": 1, "UYU": 42.5424, "VND": 25511.3726, "ZAR": 18.2516
}

def get_exchange_rate(base_currency, target_currency):
    """Fetch exchange rate from predefined data"""
    base_rate = exchange_rates.get(base_currency)
    target_rate = exchange_rates.get(target_currency)

    if base_rate is None or target_rate is None:
        print("❌ Invalid currency code.")
        return None

    return target_rate / base_rate

def convert_currency(amount, base_currency, target_currency):
    """Convert given amount to target currency"""
    rate = get_exchange_rate(base_currency, target_currency)

    if rate is None:
        print("❌ Conversion failed.")
        return None

    converted_amount = amount * rate
    return converted_amount	
while True:
    # User input
    amount = float(input("Enter the amount to convert: "))
    base_currency = input("Enter the base currency (e.g., USD, KRW, EUR): ").upper()
    target_currency = input("Enter the target currency (e.g., USD, KRW, EUR): ").upper()

    # Perform conversion
    converted_amount = convert_currency(amount, base_currency, target_currency)

    # Display result
    if converted_amount:
        print(f"💱 {amount} {base_currency} = {converted_amount:.2f} {target_currency}")

# Perform conversion
converted_amount = convert_currency(amount, base_currency, target_currency)

# Display result
if converted_amount:
    print(f"💱 {amount} {base_currency} = {converted_amount:.2f} {target_currency}")

