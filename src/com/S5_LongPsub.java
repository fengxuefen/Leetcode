package com;

public class S5_LongPsub {
	
	public String longestPalindrome(String s) {
		int maxLength = 0, beginIndex = 0 , endIndex = 0;
		int n = s.length();
		boolean[][] p = new boolean[n][n];
		for(int j = 0; j < n; j++){
			for(int i = 0; i <= j; i++){
				if(i == j || ((j == i + 1 || p[i+1][j-1]) && s.charAt(i) == s.charAt(j))){
					p[i][j] = true;
				}else{
					p[i][j] = false;
				}
				if(p[i][j] == true){
					if(maxLength < j - i + 1){
						maxLength = j - i + 1;
						beginIndex = i;
						endIndex = j + 1;
					}
				}
			}
		}
		return s.substring(beginIndex, endIndex);
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s = "ababbba";
		S5_LongPsub s5 = new S5_LongPsub();
		System.out.println(s5.longestPalindrome(s));
	}

}
