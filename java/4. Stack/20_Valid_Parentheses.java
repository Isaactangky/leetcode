// Stack and hash map
// time: O(n) iterate string once
// space: O(n) map and stack
class Solution {
    public boolean isValid(String s) {
        if (s.length() % 2 == 1) return false;
        HashMap<Character, Character> map = new  HashMap<Character, Character>();
        map.put('(', ')');
        map.put('{', '}');
        map.put('[', ']');
        Stack<Character> openPar = new Stack<Character>();
        
        for (char par : s.toCharArray()){
            //par
            if (map.containsKey(par)){
                openPar.push(par);
            }
            // par is close par
            // if last par on stack != close par -> not valid
            else if (openPar.empty()  || 
                     (map.get(openPar.pop()) != par)) {
                return false;
            }
        }
        // still have open par left
        return openPar.empty();
    }
}