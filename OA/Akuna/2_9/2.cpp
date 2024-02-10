// Problem Description: Camilla's team maintains an archaeology application used primarily by academics, researchers, and field guides. One window of the application displays a data grid of biographical information about various historical rulers along with archaeological data thereabout. Each ruler has a regnal name, which is one or more "name parts" (each separated by a single space) followed by a Roman numeral. Examples of regnal names that may appear on this page are Pedro VII (one "name part") and Alexander Pontus XV (multiple "name parts"). Note that the Roman numeral portion is always present, and it is always the last contiguous sequence of characters. Roman numerals are converted into decimal numerals using the standard procedure:
// The letter I represents 1, V represents 5, X represents 10, L represents 50, C represents 100, D represents 500, and M represents
// When two letters appear next to one another and the first is the same as the second, or represents a larger decimal value that the second, the values are added; for example, the Roman numeral XV is 10 + 5 = 15.
// When two letters appear next to one another and the first represents a smaller decimal value than the second, the value of the first is subtracted from the value of the second; for example, the Roman numeral IX is 10 - 1 = 9.
// As a larger example, the Roman numeral MMCDXLVIII is 1000 + 1000 + (500 - 100) + (50- 10) + 5 + 1 + 1 + 1 = 2448.
// Strings such as VXL, which may be valid under "alternate" translation rules, are invalid Roman numerals under the standard translation procedure.

// Problem statement: Assume that every regnal name contains a valid Roman numeral as its regnal number. Implement the following function in the code editor that sorts the rulers' names ascending, first by regnal number and then by (case-sensitive) regnal name. The function should take in the following arguments: (const std::vector<std::string> &names)

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>

using namespace std;

// Function to convert Roman numeral to integer, adhering to standard rules
int romanToInt(const string &s)
{
    unordered_map<char, int> roman{{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
    int sum = roman[s.back()];
    for (int i = s.length() - 2; i >= 0; --i)
    {
        if (roman[s[i]] < roman[s[i + 1]])
        {
            sum -= roman[s[i]];
        }
        else
        {
            sum += roman[s[i]];
        }
    }
    return sum;
}

// Comparator for sorting regnal names, with primary sorting by number, then by name
bool compareNames(const string &a, const string &b)
{
    auto split = [](const string &name) -> pair<string, int>
    {
        int i = name.size() - 1;
        while (i >= 0 && isupper(name[i]))
            --i;
        string numeral = name.substr(i + 1);
        string pureName = name.substr(0, i + 1);
        return {pureName, romanToInt(numeral)};
    };

    auto aSplit = split(a), bSplit = split(b);
    if (aSplit.second == bSplit.second)
    {
        return aSplit.first < bSplit.first;
    }
    else
    {
        return aSplit.second < bSplit.second;
    }
}

// Modified function to sort and return regnal names based on numerical value, then name
vector<string> sortRegnalNames(const vector<string> &names)
{
    vector<string> sortedNames = names;
    sort(sortedNames.begin(), sortedNames.end(), compareNames);
    return sortedNames;
}

int main()
{
    const vector<string> names = {"Nicholas VIII", "Hypapsos XXIV", "Garibald Yosef II", "Nicholas C", "Michelfranko XXIV"};
    vector<string> sortedNames = sortRegnalNames(names);

    // Print the sorted names
    for (const auto &name : sortedNames)
    {
        cout << name << endl;
    }

    return 0;
}