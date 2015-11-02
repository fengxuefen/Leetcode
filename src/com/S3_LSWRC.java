package com;
import java.util.*;

public class S3_LSWRC {
    public int lengthOfLongestSubstring(String s) {
		int max = 0;
		ArrayList<Character> sList = new ArrayList<Character>();
		for (int index = 0; index < s.length(); index++) {
			if (sList.contains(s.charAt(index))) {
				int length = sList.indexOf(s.charAt(index));
				max = max > sList.size() ? max : sList.size();
				for(int j = 0; j <= length; j++){
					sList.remove(0);
				}
			}
			sList.add(s.charAt(index));
		}
		max = max > sList.size() ? max : sList.size();
		return max;
    }
}