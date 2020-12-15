package algorithm1;

import java.util.Scanner;

//문제1 한국대의 알고리즘 기말시험 결과 10명의 학생 성적은 다음과 같다. 41점,31,48,97,9,65,27,29,13,15점이다. 
//이 학생들의 성적에 따라 낮은 점수를 받은 학생부터 순차적으로 학점을 F,D,D+,C,C+,B,B+,A,A+(2명) 을 주려고 한다.

//문제 제시 : 선택정렬을 이욯하여 성적을 오름차순으로 정렬하고,학점을 규정에 따라 부여하라
//제약 사항 : 입력 값은 0<= n <=100 인 정수 10개, 학점은 문제에서 제시된 것처럼 부여


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
