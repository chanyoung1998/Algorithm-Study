package algorithm2;

import java.util.Scanner;


//����: �ؼ��̴� ������ ��ȸ�� �����Ͽ���. ��ȸ�� �����ϴ� �縧���� ��ȸ� �����κ��� ���� �������� ��ȣǥ�� �޾Ҵ�. ������
//���Ͽ� �ؼ��̴� 31�� ��ȣ�츦 �޾Ҵ�. �׸��� �����ڵ���  35 9 8 18 98 31 58 17 76 45 ������ �����Ͽ���. 
//��ȸ� ���� ������ ������ ��ȸ ������ ���� �����ڵ��� �ٽ� ��ȣ������ ���� ������� �Ѵ�.
//�ؼ��̴� �տ��� �� ��°�� ���� �Ǵ°�?

//��������: ���������� �̿��Ͽ� ������������ �����ڵ��� �����϶�.
//�������: �Է°��� ������ 1<= N <= 99�� �Ѵ�.



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
					System.out.println("��ġ�� �˰��� �ϴ� ������ �Է��Ͻÿ�");
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
						System.out.println((i+1) + "�� °�� ���� �˴ϴ�" );
					
					
				}
		
	}

}
