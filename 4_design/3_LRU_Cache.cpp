// LRU Cache

/*
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
*/

// my solution
class LRUCache {
public:
    int m_capacity;
    unordered_map<int, list<pair<int, int>>::iterator> m_map;
    list<pair<int, int>> m_list;
    
    LRUCache(int capacity) {
        m_capacity = capacity;
    }
    
    int get(int key) {
        auto it = m_map.find(key);
        
        if (it == m_map.end())
            return -1;
        
        m_list.splice(m_list.begin(), m_list, it->second);
        return it->second->second;
    }
    
    void put(int key, int value) {
        auto it = m_map.find(key);
        
        if (it != m_map.end()) {
            m_list.splice(m_list.begin(), m_list, it->second);
            it->second->second = value;
            
            return;
        }
        
        if (m_map.size() == m_capacity) {
            int key_del = m_list.back().first;
            m_list.pop_back();
            m_map.erase(key_del);
        }
        
        m_list.emplace_front(key, value);
        m_map[key] = m_list.begin();
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */