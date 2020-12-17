package alrgorithm3;

public class MergeSort {
	static int[] buff;
	
	static void __mergeSort(int[] a , int left, int right )
	{
		if(left< right )
		{
			int i ;
			int center = (left + right) / 2 ;
			int p = 0 ; 
			int j= 0;
			int k = left;
			
			
			__mergeSort(a,left,center);
			__mergeSort(a,center+1,right);
			
			for(i = left; i <=center ; i ++)
				buff[p++] = a[i];
			
			
			while(i <=right  && j <p)
				a[k++] = (buff[j] <= a[i]) ? buff[j++] : a[i++];
			
			while(j < p )
				a[k++] = buff[j++];
			
		}
	}
	
	static void mergeSort(int[] a , int n)
	{
		buff = new int[n];
		
		__mergeSort(a,0,n-1);
		
		buff = null;
	}
}
