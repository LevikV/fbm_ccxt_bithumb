import ccxt_patch
import asyncio

async def main():
    api_key = 'd3c87b3747b043ecbc5672d5e15c11bc'
    api_secret = '2EF5C2B8EB044466435F5E510E82AFF1'
    
    params = {
        'apiKey': api_key,
        'secret': api_secret,
        'timeout': 50000,
    }
    symbol = 'XRP/USDT'
    symbol_swap = 'XRP/USDT:USDT'
    market_id = 'XRPUSDT'

    exchange_client = ccxt_patch.hotcoin(params)
    
    try:
        await exchange_client.load_markets()
        market_1 = exchange_client.safe_market(market_id, None, None, 'spot')
        data = await exchange_client.fetch_markets()
    finally:
        await exchange_client.close()
    
    market = data[symbol]
    market_swap = data[symbol_swap]
    print(market_1)
    print(market)
    print(market_swap)

if __name__ == '__main__':
    asyncio.run(main())

