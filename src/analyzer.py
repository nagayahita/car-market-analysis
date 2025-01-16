analyzer = CarMarketAnalyzer(processed_train)


overview = analyzer.create_market_overview()


print("=== 🚗 MARKET ANALYSIS REPORT ===")
print("\n📊 MARKET SIZE:")
for key, value in overview["Market Size"].items():
    print(f"• {key}: {value:,}")

print("\n💰 PRICE OVERVIEW:")
for key, value in overview["Price Overview"].items():
    print(f"• {key}: {value}")

print("\n🏆 TOP MANUFACTURERS BY PRICE:")
for name, price in overview["Top Manufacturers"]["Most Expensive"].items():
    print(f"• {name}: {price}")

print("\n📈 POPULAR MANUFACTURERS BY VOLUME:")
for name, count in overview["Top Manufacturers"]["Most Popular"].items():
    print(f"• {name}: {count:,} units")

print("\n🚙 TOP CATEGORIES BY PRICE:")
for category, price in overview["Popular Categories"]["By Average Price"].items():
    print(f"• {category}: ${price:,.2f}")
