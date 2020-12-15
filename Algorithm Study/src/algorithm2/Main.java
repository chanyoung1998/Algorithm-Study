package algorithm2;

import java.util.Scanner;


//문제: 준성이는 마라톤 대회에 출전하였다. 대회에 출전하는 사름들은 대회운영 측으로부터 각자 무작위로 번호표를 받았다. 마라톤
//당일에 준성이는 31번 번호펴를 받았다. 그리고 출전자들은  35 9 8 18 98 31 58 17 76 45 순으로 입장하였다. 
//대회운영 측은 공정한 마라톤 대회 진행을 위해 출전자들을 다시 번호순으로 줄을 세우려고 한다.
//준성이는 앞에서 몇 번째에 서게 되는가?

//문제제시: 삽입정렬을 이용하여 오름차순으로 출전자들을 정렬하라.
//제약사항: 입력값의 범위는 1<= N <= 99로 한다.



public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc=new Scanner(System.in);
		int [] arr = new int[10];
				
				for(int i = 0 ; i < arr.length ; i ++)
				{
					int num = sc.nextInt();
					
					while(!(num >= 0 &&num <= 100)) {
						num = sc.nextInt();
					}
					
					arr[i] = num;
				}
				
				
				boolean flag = false;
				int num = 0 ;
				
				while(!flag)
				{
					System.out.println("위치를 알고자 하는 정수를 입력하시오");
					 num = sc.nextInt();
					
					for(int i = 0 ; i < arr.length; i ++)
					{
						if(num == arr[i])
						{
							flag = true;
							break;
						}
					}
					
				}
				
				for(int i = 1 ; i < arr.length; i ++)
				{
					int j;
					int tmp = arr[i];
					
					for( j = i ; j >0 && arr[j-1] > tmp; j--)
					{
						arr[j] = arr[j-1];
					}
					
					arr[j] = tmp;
				}
				
				for(int i = 0 ;  i < arr.length; i++) {
					
					if(arr[i] == num)
						System.out.println((i+1) + "번 째로 서게 됩니다" );
					
					
				}
		
	}

}
