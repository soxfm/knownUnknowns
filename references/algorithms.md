----
title: algo written in ruby
slugs: algorithms
category: [ 'references', 'knowledge', 'programming','methods', 'models' ]
date: 2020-1-15
----

# Algorithms.rb

---
```ruby
def partition arr, lo, hi  
  i,j = lo+1,hi
  while true
    i+=1 while arr[i] <= arr[lo] and i < hi
    j-=1 while arr[j] > arr[lo] and j > lo
    break if i>=j
    arr[i], arr[j] = arr[j], arr[i] #swap
  end
  arr[lo], arr[j] = arr[j], arr[lo]
  j
end

def quicksort arr, lo = 0, hi = nil  
  hi ||= arr.size - 1
  return arr if hi <= lo
  pivot = partition arr, lo, hi
  quicksort arr, lo, pivot-1
  quicksort arr, pivot+1, hi
end

#test
p quicksort [3,4,2,6,56,14,33,1,9,6] #[1, 2, 3, 4, 6, 6, 9, 14, 33, 56]
```

```ruby
def merge_sort(lst)
  return lst if lst.length <= 1
  mid = lst.length / 2
  left = merge_sort(lst[0..mid - 1])
  right = merge_sort(lst[mid..lst.length])
  merge(left, right)
end

def merge(left, right)  
  result = []; i = j = 0;
  while i < left.size and j < right.size
    if left[i] <= right[j]
      result << left[i]; i+=1;
    else
      result << right[j]; j+=1;
    end
  end
  while i<left.size do 
    result << left[i]; i+=1;
  end
  while j<right.size
    result << right[j]; j+=1;
  end
  result
end

#test
p merge_sort [4,3,6,1,2,7,8,5,9,0] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```ruby
def unique_bsts(n)
  a = Array.new(n+1, 0)
  a[0] = a[1] = 1

  (2..n).each do |i|
    (1..i).each do |j|
      a[i] += (a[j-1] * a[i-j])
    end
  end

  return a[n]
end

p unique_bsts(4) # => 14
```