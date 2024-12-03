function fibonacci(n) {
    if (n < 0) {
      throw new Error("Input harus bilangan positif atau nol");
    }
    if (n === 0) {
      return [0];
    } else if (n === 1) {
      return [0, 1];
    }
    const fibSeries = fibonacci(n - 1);
    fibSeries.push(fibSeries[fibSeries.length - 1] + fibSeries[fibSeries.length - 2]);
    return fibSeries;
  }
  

// Jangan hapus kode di bawah ini!
export default fibonacci;
