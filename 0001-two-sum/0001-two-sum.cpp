class Solution {
private:
    struct Entry {
        int32_t  key;
        int16_t  index;
        uint16_t gen;
    };

    static_assert(sizeof(Entry) == 8);

    static constexpr uint32_t SIZE = 1u << 15; // 32768
    static constexpr uint32_t MASK = SIZE - 1;

    static uint32_t hash(int32_t x) {
        uint32_t h = static_cast<uint32_t>(x);

        h ^= h >> 16;
        h *= 0x7feb352d;
        h ^= h >> 15;
        h *= 0x846ca68b;
        h ^= h >> 16;

        return h;
    }

    Entry table[SIZE]{};
    uint16_t gen = 0;

public:

    vector<int> twoSum(vector<int>& nums, int target) {
        // Real memset only once every 65535 calls.
        if (++gen == 0) [[unlikely]] {
            std::memset(table, 0, sizeof(table));
            gen = 1;
        }

        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            int32_t value = nums[i];
            int32_t required = target - value;

            // Find the complement.
            uint32_t index = hash(required) & MASK;

            while (table[index].gen == gen) {
                if (table[index].key == required) {
                    return {
                        static_cast<int>(table[index].index),
                        i
                    };
                }

                index = (index + 1) & MASK;
            }

            // Insert current value.
            index = hash(value) & MASK;

            while (table[index].gen == gen &&
                   table[index].key != value) {
                index = (index + 1) & MASK;
            }

            table[index].key   = value;
            table[index].index = static_cast<int16_t>(i);
            table[index].gen   = gen;
        }

        return {};
    }
};