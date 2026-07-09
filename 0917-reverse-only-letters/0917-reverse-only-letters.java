class Solution {
    public static boolean isletter(char ch){

        ch = Character.toLowerCase(ch);

        if (97 <= ch && ch <= 122){
            return true;
        }

        return false;
    }
    public String reverseOnlyLetters(String s) {

        char[] arr = s.toCharArray();
        int i = 0;
        int j = arr.length-1;

        while (i < j){

            while (!(isletter(arr[i])) && i < j){
                i++;
            }
            while (!(isletter(arr[j])) && i < j){
                j--;
            }

            char temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;

            i++;
            j--;
        }

        return new String(arr);

    }
}
