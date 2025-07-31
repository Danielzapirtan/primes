#include <stdio.h>
#include <stdlib.h>

#ifdef HAS64BIT
typedef unsigned long u;
#else
typedef unsigned u;
#endif

int pr(u p) {
  u k = (u) 3;
  while (k <= p / k) {
    if (p % k == 0)
	    return 0;
    k += (u) 2;
  }
  return 1;
}

int gbn(u n) {
  u p = (u) 3;
  while (p <= n - p) {
    if (pr(p))
      if (pr(n - p))
        return 1;
    p += 2;
  }
  return 0;
}

int gbab(u a, u b) {
  u n = a;
  while (n <= b) {
    if (gbn(n) == 0)
      return 0;
    n += 2;
  }
  return 1;
}

int main(int argc, char **argv) {
  u a;
  u b;
#ifdef HAS64BIT
  sscanf(argv[1], "%lu", &a);
  sscanf(argv[2], "%lu", &b);
#else
  sscanf(argv[1], "%u", &a);
  sscanf(argv[2], "%u", &b);
#endif
  return (gbab(a, b) == 0);
}

