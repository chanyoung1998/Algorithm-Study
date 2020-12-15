package algorithm1;

import java.util.Scanner;

//����1 �ѱ����� �˰��� �⸻���� ��� 10���� �л� ������ ������ ����. 41��,31,48,97,9,65,27,29,13,15���̴�. 
//�� �л����� ������ ���� ���� ������ ���� �л����� ���������� ������ F,D,D+,C,C+,B,B+,A,A+(2��) �� �ַ��� �Ѵ�.

//���� ���� : ���������� �̟G�Ͽ� ������ ������������ �����ϰ�,������ ������ ���� �ο��϶�
//���� ���� : �Է� ���� 0<= n <=100 �� ���� 10��, ������ �������� ���õ� ��ó�� �ο�


public class Main {

	public enum Grade{
		
	}
	
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Student [] std = new Student[10];
		Scanner sc=new Scanner(System.in);
		
		for(int i = 0 ; i < 10 ; i ++)
		{
			int score = sc.nextInt();
			
			while(!(score >= 0 &&score <= 100)) {
				score = sc.nextInt();
			}
			
			std[i] = new Student(score);
		}
		
	
		for(int i = 0 ; i < std.length - 1 ; i ++)
		{
			int min = i;
			
			for(int j = i+1; j < std.length; j ++)
			{
				if(std[j].getScore() < std[min].getScore())
					min = j;
			}
			
			swap(std,i,min);
		}

		
		for(int i = 0 ; i <10 ; i++)
		{
			switch(i) { 
			case 0:
				std[i].setGrade("F");
				break;
			case 1:
				std[i].setGrade("D");
				break;
			case 2:
				std[i].setGrade("D+");
				break;
			case 3:
				std[i].setGrade("C");
				break;
			case 4:
				std[i].setGrade("C+");
				break;
			case 5:
				std[i].setGrade("B");
				break;
			case 6:
				std[i].setGrade("B+");
				break;
			case 7:
				std[i].setGrade("A");
				break;
			case 8:
				std[i].setGrade("A+");
				break;
			case 9:
				std[i].setGrade("A+");
				break;
			}
		}
		
		for(Student std1 : std) {
			System.out.println(std1.getScore() + "," + std1.getGrade());
			
		}
		
		
		
		return;
		
		
	
	}

	
	public static void swap(Student[] std, int i, int j)
	{
		Student temp = new Student(std[i].getScore());
		
		std[i].setScore(std[j].getScore());
		std[j].setScore(temp.getScore());
		
	}
	
}
