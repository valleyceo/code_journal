// jdurie
#pragma GCC target ("avx2")
#pragma GCC optimize ("O3")
#pragma GCC optimize ("unroll-loops")
#include <bits/stdc++.h>
using namespace std;
template<class T, class S>
ostream& operator << (ostream &o, const pair<T, S> &p) {
    return o << '(' << p.first << ", " << p.second << ')';
}
template<template<class, class...> class T, class... A>
typename enable_if<!is_same<T<A...>, string>(), ostream&>::type
operator << (ostream &o, T<A...> V) {
	o << '[';
	for(auto a : V) o << a << ", ";
	return o << ']';
}

typedef long long int ll;
typedef long double ld;
typedef pair<ll, ll> pl;

#define G(x) ll x; cin >> x;
#define GD(x) ld x; cin >> x;
#define GS(s) string s; cin >> s;
#define F(i, l, r) for(ll i = l; i < r; i++)
#define FD(i, r, l) for(ll i = r; i > l; i--)
#define P(a, n) { cout << "{ "; F(_, 0, n) cout << a[_] << " "; cout << "}" << endl; }
#define EX(x) { cout << x << endl; exit(0); }
#define K first
#define V second
#define M 1000000007 //998244353
#define N 1610

ll r, s, deck[N];
vector<pl> ans;

bool sorted(ll i1, ll i2) {
    F(i, i1, i2 - 1) if(deck[i] > deck[i + 1]) return false;
    return true;
}

void swp(int a, int b) {
    ans.push_back({a, b});
    vector<ll> temp;
    F(i, 0, a) temp.push_back(deck[i]);
    for(ll i = 0; i < b; i++) deck[i] = deck[a + i];
    for(ll i = b; i < a + b; i++) deck[i] = temp[i - b];
}

bool needLastFix() {
    ll lastMax = -1;
    while(deck[lastMax + 1] == r - 1) lastMax++;
    if(sorted(lastMax + 1, r * s)) {
        swp(lastMax + 1, r * s - lastMax - 1);
        return true;
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    G(T) F(w, 1, T + 1) {
        cin >> r >> s;
        ans.clear();
        ll idx = 0;
        F(i, 0, s) F(j, 0, r) deck[idx++] = j;
        while(!sorted(0, r * s)) {
            if(needLastFix()) break;
            ll p1 = r * s - 1;
            while(p1 != 1 && (deck[p1 - 1] != deck[0] || deck[p1] == deck[p1 - 1])) p1--;
            if(p1 == 1) cout << "PROBLEM" << endl;
            ll p2 = p1 - 1;
            while(p2 >= 0 && deck[p2] != deck[p1]) p2--;
            if(p2 == -1) cout << "PROBLEM" << endl;
            swp(p2 + 1, p1 - p2 - 1);
        }
        cout << "Case #" << w << ": " << ans.size() << endl;
        for(pl p : ans) cout << p.K << " " << p.V << endl;
    }
}