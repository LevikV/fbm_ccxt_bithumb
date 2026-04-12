import ccxt_patch
import asyncio

async def main():
    exchange_client = ccxt_patch.bithumb()
    
    try:
        data = await exchange_client.fetch_listings()
    finally:
        await exchange_client.close()
    
    print(data)

if __name__ == '__main__':
    asyncio.run(main())

