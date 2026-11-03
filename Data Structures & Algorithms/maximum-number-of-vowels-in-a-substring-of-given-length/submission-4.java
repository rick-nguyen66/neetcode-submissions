class Solution {
    public int maxVowels(String s, int k) {
        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');

        int r = 0;
        int l = 0;
        int max_len = 0;
        int len = 0;

        // in one loop, shift r forward until window is larger than k (be sure to monitor len)
        // when window is larger, move l forward... adjust len if first char is a vowel
        while (r < s.length()) {
            if (max_len == k) return k;
            if (vowels.contains(s.charAt(r++))) len++;
            max_len = Math.max(max_len, len);

            if (r - l < k) continue;
            if (vowels.contains(s.charAt(l++))) len--;
        }

        return max_len;
    }
}
