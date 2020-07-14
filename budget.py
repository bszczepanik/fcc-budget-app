class Category:
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.value_list = []
        self.op_list = []

    def __str__(self):
        name_width = len(self.name)
        line_width = 30
        lines = []

        # Heading
        line = "*" * int((line_width - name_width)/2) \
            + self.name
        line += "*" * (line_width - len(line)) \
            + "\n"
        lines.append(line)

        # Operation list loop
        for i in range(len(self.value_list)):
            line = self.op_list[i][:23]
            line += " " * \
                (line_width - len(line) - len(self.value_list[i]))
            line += (self.value_list[i])
            line += "\n"
            lines.append(line)

        # Summary
        lines.append("Total: %.2f" % (self.value))

        return "".join(lines)

    def deposit(self, value, operation=""):
        self.value += value
        self.value_list.append("+%.2f" % value)
        self.op_list.append(operation)

    def withdraw(self, value, operation=""):
        self.value -= value
        self.value_list.append("-%.2f" % value)
        self.op_list.append(operation)

    def transfer(self, value, target):
        self.withdraw(value, ("Transfer to " + target.name.capitalize()))
        target.deposit(value, ("Transfer from " + self.name.capitalize()))

    def get_balance(self):
        return self.value


def create_spend_chart(categories):
    percent_list = list(range(100, -1, -10))
    spended_list = list(map(spended_money, categories))
    spended_percent = [int(round(x/sum(spended_list), 1)
                           * 100) for x in spended_list]
    print("spended_list", spended_list)
    print("spended_percent", spended_percent)
    lines = []

    for item in percent_list:
        item_str = str(item)
        line = " " * (3 - len(item_str)) \
            + item_str + "| "
        for cat in range(len(categories)):
            if spended_percent[cat] >= item:
                line += "o  "
            else:
                line += "   "
        line += "\n"
        lines.append(line)

    line = "    ----------"
    lines.append(line)

    return "".join(lines)


def spended_money(x):
    result = 0

    for item in x.value_list:
        if float(item) < 0:
            result += float(item) * (-1)
    return result
