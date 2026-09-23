class Solution {
    public boolean isAnagram(String s, String t) {
        char[] arrs = s.toCharArray();
        char[] arrt = t.toCharArray();
        Arrays.sort(arrs);
        Arrays.sort(arrt);
        String news = String.valueOf(arrs);
        String newt = String.valueOf(arrt);

        if(news.equals(newt)){
            return true;
        }
        else{
            return false;
        }
    }
}
