// Problem description: The Komodo Dragon Trading Company is the newest participant on the Grand Monitor Stock Exchange, a peculiar marketplace that lists companies specializing in, or otherwise concerning, reptiles. Over the course of the trading day, the Komodo Dragon Trading Company listens to the exchange feed for updates to stock prices while simultaneously placing buy and sell orders against other organizations competing in the market. When the exchange processes a buy or a sell order, it uses the current price of the target stock to calculate the profits from the sale or the cost of the purchase; the current price is calculated by starting at some daily baseline price and cumulatively applying all of the price updates for the target stock up to the time when the order was placed, with a minimum possible price of 1. There is no limit to the number of orders that a single participant can place over the course of a day, nor is there a limit to the quantity of stock that can be bought or sold in a single order. Orders may be placed for zero quantity.
// Assume that every order is successfully executed. Complete the following function in the code editor to determine the profit and/or loss for the Komodo Dragon Trading Company on each stock that it either bought or sold over the course of the trading day.

// The following auxiliary types are defined for you:

/// The definition of a buy or a sell order targeting a particular stock in the market.
/// member timestamp The time at which the order request was made.
/// @member stockId The ID of the stock to either buy or sell.
/// member buy Whether the order is to buy ('true') or sell (' false') shares of the stock.
/// member quantity The number of shares of the stock to buy or sell.
struct Order
{
    int timestamp;
    int stockId;
    bool buy;
    int quantity;
};

/// The definition of an update to the price of a stock.
/// @member timestamp The time at which the change in price took effect.
/// @member stockId The ID of the stock whose price changed.
/// @member delta The amount that the stock's price increased (if positive) or decreased (if negative).
struct PriceUpdate
{
    int timestamp;
    int stockId;
    int delta;
};

#include <vector>
#include <iostream>

/// @param initialPrice The price of all stocks at the beginning of the day, before any price updates are published.
/// @param orders The sequence of buy and sell orders to be executed. /// @param feed The exchange feed of price updates to various stocks.
/// pre @p initialPrice >= 1.
/// @pre @p orders is not empty, and is sorted in ascending order by timestamp.
/// @pre @p feed is not empty, and is sorted in ascending order by timestamp.
/// @pre @p The set of all timestamps among orders in @p orders and price updates in @p feed contains no duplicates.
/// @returns A collection [see below] with the end-of-day profits and losses of each stock for which at least one order was executed. Stocks for which a price update was published but no orders were executed should be excluded from the return value.

#include <iostream>
#include <vector>
#include <map>

using namespace std;

struct Order
{
    int timestamp;
    int stockId;
    bool buy;
    int quantity;
};

struct PriceUpdate
{
    int timestamp;
    int stockId;
    int delta;
};

map<int, long long> calculateProfitsAndLosses(int initialPrice, const vector<Order> &orders, const vector<PriceUpdate> &feed)
{
    // Maps to keep track of the latest price of each stock and the profit/loss
    map<int, int> currentPrices;
    map<int, long long> profitLoss;

    // Initialize current prices with the initial price
    for (const auto &order : orders)
    {
        currentPrices[order.stockId] = initialPrice;
    }

    size_t feedIndex = 0;
    size_t feedSize = feed.size();

    // Process each order
    for (const auto &order : orders)
    {
        // Update prices based on price updates before this order's timestamp
        while (feedIndex < feedSize && feed[feedIndex].timestamp <= order.timestamp)
        {
            const auto &update = feed[feedIndex++];
            currentPrices[update.stockId] = max(1, currentPrices[update.stockId] + update.delta);
        }

        // Calculate profit or loss from this order
        if (order.buy)
        {
            // Buying stock: decrease profit/loss by the cost of purchase
            profitLoss[order.stockId] -= currentPrices[order.stockId] * order.quantity;
        }
        else
        {
            // Selling stock: increase profit/loss by the revenue from sale
            profitLoss[order.stockId] += currentPrices[order.stockId] * order.quantity;
        }
    }

    return profitLoss;
}

int main()
{
    int initialPrice = 10;
    vector<Order> orders = {
        {0, 2, true, 15},
        {4, 1, false, 30},
        {6, 1, true, 10},
        {10, 2, true, 5},
        {15, 4, false, 100}};
    vector<PriceUpdate> feed = {
        {3, 1, +4},
        {5, 1, -1},
        {8, 2, +2},
        {12, 3, -5}};

    auto result = calculateProfitsAndLosses(initialPrice, orders, feed);

    // Print the results
    for (const auto &item : result)
    {
        cout << "Stock ID: " << item.first << ", Profit/Loss: " << item.second << endl;
    }

    return 0;
}