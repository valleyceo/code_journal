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
#define N 100010

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    G(T) F(w, 1, T + 1) {
        cout << "Case #" << w << ": ";
        G(a) G(b)
        string s;
        F(k, 1, 50) {
            if(a == 0 && b == 0) {
                cout << s << endl;
                break;
            }
            if(abs(a) % 2 == abs(b) % 2) {
                cout << "IMPOSSIBLE" << endl;
                break;
            }
            if(abs(a) + abs(b) == 1) {
                if(a == 1) s += "E";
                if(a == -1) s += "W";
                if(b == 1) s += "N";
                if(b == -1) s += "S";
                a = b = 0;
            }
            if(a % 2) {
                bool bB = b % 4, bA = (a + 1) % 4;
                if(bB != bA) { s += "W"; a++; }
                else { s += "E"; a--; }
            }
            if(b % 2) {
                bool bA = a % 4, bB = (b + 1) % 4;
                if(bA != bB) { s += "S"; b++; }
                else { s += "N"; b--; }
            }
            a /= 2; b /= 2;
        }
    }
}  