volume = int(input())
first_pipe_debit = int(input())
second_pipe_debit = int(input())
hours = float(input())

first_pipe_volume = first_pipe_debit * hours
second_pipe_volume = second_pipe_debit * hours
volume_for_hours = first_pipe_volume + second_pipe_volume

if volume >= volume_for_hours:
    fullness_percent = volume_for_hours * 100 / volume
    first_pipe_percent = first_pipe_volume * 100 / volume_for_hours
    second_pipe_percent = second_pipe_volume * 100 / volume_for_hours
    print(
        f"The pool is {fullness_percent:.2f}% full."
        f" Pipe 1: {first_pipe_percent:.2f}%. Pipe 2: {second_pipe_percent:.2f}%.")

else:
    overflow = volume_for_hours - volume
    print(f"For {hours} hours the pool overflows with {overflow:.2f} liters.")
