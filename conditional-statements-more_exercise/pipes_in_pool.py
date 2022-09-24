pool_volume = int(input())
first_pipe_debit = int(input())
second_pipe_debit = int(input())
hours_worker = float(input())

first_pipe_filled = first_pipe_debit * hours_worker
second_pipe_filled = second_pipe_debit * hours_worker
total_filled = first_pipe_filled + second_pipe_filled
total_filled_percentage = total_filled * 100 / pool_volume
first_pipe_percentage = first_pipe_filled * 100 / total_filled
second_pipe_percentage = second_pipe_filled * 100 / total_filled

if total_filled <= pool_volume:
    print(f"The pool is {total_filled_percentage:.2f}% full. "
          f"Pipe 1: {first_pipe_percentage:.2f}%. Pipe 2: {second_pipe_percentage:.2f}%.")
else:
    print(f"For {hours_worker} hours the pool overflows with {total_filled - pool_volume:.2f} liters.")
