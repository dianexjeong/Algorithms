// insertion sort

#include <stdio.h>
#include <stdlib.h>
int* insertion(int x, int* a) {
  int i = 0, j = 0, key = 0;
  for (i = 1; i < x; i++) {
    key = a[i];
    j = i - 1;
    while ((j > -1) && (a[j] > key)) {
      a[j + 1] = a[j];  //두 개 순서를 바꾸는것
      j -= 1;
    }
    a[j + 1] = key;
  }
  return (int*)a;
}

void printarr(int x, int* a) {
  int i = 0;
  for (i = 0; i < x; i++) {
    printf("%d\n", a[i]);
  }
  return;
}
int main() {
  int count = 0;
  scanf("%d", &count);
  int A[count];
  int i = 0;

  for (i = 0; i < count; i++) {
    scanf("%d", &A[i]);
  }

  int* Arr = insertion(count, A);
  printarr(count, Arr);
  return 0;
}