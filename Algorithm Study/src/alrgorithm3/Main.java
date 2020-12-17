package alrgorithm3;

import java.util.Scanner;

//문제:준성이가 컴퓨터 파일 정리를 하고 있다. 필요 없는 파일을 삭제하고 남은 파일을 순서대로 나열하고 싶다. 파일 이름이 숫자로 되어 있다.
//문제제시:남은 파일을 병합정렬 알고리즘을 이용하여 오름차순으로 정렬하라


public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		
		
		for(int i = 0 ; i < n ; i ++)
		{
			int input = sc.nextInt();
			arr[i] = input;
		}
		
		MergeSort.mergeSort(arr,n);
		
		for(int a : arr)
			System.out.print(a + " ");
			
		
	}

}
