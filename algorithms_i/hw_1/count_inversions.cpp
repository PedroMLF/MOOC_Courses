#include <iostream>
#include <fstream>
#include <cstdlib>

long long count_split_inv(long array[], long lower, long mid, long upper){

    long left_pos = lower;
    long left_end = mid;
    long right_pos = mid+1;
    long right_end = upper;

    // No need to add one because the first index is 0
    long tmp_values[upper - lower];
    long long nr_inversions = 0;
    long i = 0;

    long k;

    while ((left_pos <= left_end) && (right_pos <= right_end)){
        if (array[left_pos] <= array[right_pos]){
            tmp_values[i] = array[left_pos];;
            i++;
            left_pos++;
        }
        else {
            nr_inversions = nr_inversions + (left_end - left_pos + 1);
            tmp_values[i] = array[right_pos];
            i++;
            right_pos++;
        }
    }

    // When the previous while finishes we have to parse one
    // of the sides until the end
    if (left_pos > left_end){
        for (k = right_pos; k <= right_end; k++, i++){
            tmp_values[i] = array[k];
        }
    }
    else {
        for (k = left_pos; k <= left_end; k++, i++){
            tmp_values[i] = array[k];
        }
    }

    // Merge the resulting array into the array
    for (k = lower; k <= upper; k++){
        array[k] = tmp_values[k - lower];
    }

    return nr_inversions;

}

long long count(long array[], long lower, long upper){

    long mid = lower + (upper - lower) / 2;
    if (lower >= upper){
        return 0;
    }
    else {
        long nr_left_inversions = count(array, lower, mid);
        long nr_right_inversions = count(array, mid + 1, upper);
        long nr_split_inversions = count_split_inv(array, lower, mid, upper);
        return nr_left_inversions + nr_right_inversions + nr_split_inversions;
    }
}

int main(){

    std::ifstream file("IntegerArray.txt");
    std::string line;

    // Get the number of lines in the file
    int nr_lines = 0;

    while (std::getline(file, line)){
        nr_lines ++;
    }

    std::cout << "Number of lines: " << nr_lines << std::endl;

    // Read once again to fill the array
    file.clear();
    file.seekg(0);

    long values[nr_lines];
    long value;
    long i = 0;

    while (std::getline(file, line)){
        value = atoi(line.c_str());
        values[i] = value;
        i++;
    }

    std::cout << "Number of parsed values: " << i << std::endl;

    // Calculate the number of inversions
    long nr_inversions = count(values, 0, nr_lines-1);
    std::cout << "Number of inversions: " << nr_inversions << std::endl;

    return 0;

}
