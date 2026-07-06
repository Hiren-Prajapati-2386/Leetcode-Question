class Solution {

    public static void reverse(char[] arr,int start,int end){

        while (start < end){
            char temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }

    public String reverseWords(String s) {

        char[] arr = s.toCharArray();
        int n = arr.length;
        int start = 0;

        for (int end = 0; end <= n; end++) {

            if(end == n || arr[end] == ' '){
                reverse(arr,start,end-1);
                start = end + 1;
            }

        }

        return new String(arr);
        
    }
}