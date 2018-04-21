// Saving The Universe Again

/*
Problem link:
https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard
*/

// my solution
#include <iostream>
#include <string>

int compute_damage(std::string s) {
	int strength = 1, damage = 0;
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == 'C')
			strength *= 2;
		else if (s[i] == 'S')
			damage += strength;
	}

	return damage;
}

int main()
{
	int T, n;
	T = 1;
	
	std::cin >> n;

	while (T <= n)
	{
		std::string s_in; // instruction
		int D, damage; // shield, damage
		bool is_hacked = true;
		int hack_count = 0;
        
        std::cin >> D;
		std::cin >> s_in;
		
		damage = compute_damage(s_in);

		while (damage > D && is_hacked) {
			is_hacked = false;
			for (int i = s_in.length()-1; i > 0; i--) {
				if (s_in[i-1] == 'C' && s_in[i] == 'S') {
					s_in[i-1] = 'S';
					s_in[i] = 'C';
					is_hacked = true;
					damage = compute_damage(s_in);
					hack_count++;
					break;
				}
			}
		}

		if (!is_hacked) {
			std::cout << "Case #" << std::to_string(T) << ": " << "IMPOSSIBLE" << '\n';
		} else {
			std::cout << "Case #" << std::to_string(T) << ": " << hack_count << '\n';
		}
		
		T++;
	}
	
	return 0;
}