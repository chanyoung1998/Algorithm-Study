package alrgorithm3;

import java.util.Scanner;

//����:�ؼ��̰� ��ǻ�� ���� ������ �ϰ� �ִ�. �ʿ� ���� ������ �����ϰ� ���� ������ ������� �����ϰ� �ʹ�. ���� �̸��� ���ڷ� �Ǿ� �ִ�.
//��������:���� ������ �������� �˰����� �̿��Ͽ� ������������ �����϶�


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
