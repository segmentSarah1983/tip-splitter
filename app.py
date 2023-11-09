"""Split a meal bill. Run: python3 app.py 80 --tip 15 --people 4"""
import argparse
from decimal import Decimal, ROUND_UP


def split_bill(bill, tip, people):
    if not bill.is_finite() or not tip.is_finite() or bill < 0 or tip < 0:
        raise ValueError("Bill and tip must be finite and nonnegative")
    if people < 1:
        raise ValueError("At least one person is required")
    total = bill * (1 + tip / 100)
    return (total / people).quantize(Decimal("0.01"), rounding=ROUND_UP)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bill", type=Decimal)
    parser.add_argument("--tip", type=Decimal, default=Decimal("15"))
    parser.add_argument("--people", type=int, default=1)
    args = parser.parse_args()
    try:
        print(f"Each person pays: {split_bill(args.bill, args.tip, args.people):.2f}")
    except ValueError as error:
        parser.error(str(error))
