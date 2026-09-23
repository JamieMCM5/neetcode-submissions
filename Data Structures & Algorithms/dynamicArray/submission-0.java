class DynamicArray {
    int[] arr = new int[0];
    int capacity = 0;
    int size = 0;
    int count = 0;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.arr = new int[capacity];
        this.size = 0;

    }

    public int get(int i) {
        return this.arr[i];
    }

    public void set(int i, int n) {
        this.arr[i] = n;
    }

    public void pushback(int n) {
        if(this.size == this.capacity){
            this.resize();
        }
        this.arr[this.size] = n;
        this.size++;
    }

    public int popback() {
        int popped = this.arr[this.size - 1];
        this.arr[this.size - 1] = 0;
        this.size--;
        return popped;
    }

    public void resize() {
        this.capacity = this.capacity * 2;
        int[] newArr = new int[this.capacity];
        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }
        this.arr = newArr;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.capacity;
    }
}
