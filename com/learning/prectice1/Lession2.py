# Create if else conditions


def calc_weekly_wages(totalHours, hourlyWage):
    '''Return the total weekly wages for a worker working totalHours,
    with a given regular hourlyWage.  Include overtime for hours over 40.
    '''
    if totalHours <= 40:
        totalWages = hourlyWage*totalHours
    else:
        overtime = totalHours - 40
        totalWages = hourlyWage*40 + (1.5*hourlyWage)*overtime
    return totalWages


def main():
    hours = float(input('Enter hours worked: '))
    wage = float(input('Enter dollars paid per hour: '))
    total = calc_weekly_wages(hours, wage)
    print('Wages for {hours} hours at Rs{wage:.2f} per hour are Rs{total:.2f}.'
          .format(**locals()))


main()

