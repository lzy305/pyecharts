import os
import random

from pyecharts.render import make_snapshot


def render_chart_images(charts: list):
    for fn, name in charts:
        make_snapshot(fn().render(), Faker.img_path(name + ".png"))


class _Faker:
    clothes = ["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"]
    drinks = ["可乐", "雪碧", "橙汁", "绿茶", "奶茶", "百威", "青岛"]
    phones = ["小米", "三星", "华为", "苹果", "魅族", "VIVO", "OPPO"]
    fruits = ["草莓", "芒果", "葡萄", "雪梨", "西瓜", "柠檬", "车厘子"]
    animal = ["河马", "蟒蛇", "老虎", "大象", "兔子", "熊猫", "狮子"]
    cars = ["宝马", "法拉利", "奔驰", "奥迪", "大众", "丰田", "特斯拉"]
    dogs = ["哈士奇", "萨摩耶", "泰迪", "金毛", "牧羊犬", "吉娃娃", "柯基"]
    week = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    week_en = "Saturday Friday Thursday Wednesday Tuesday Monday Sunday".split()
    clock = (
        "12a 1a 2a 3a 4a 5a 6a 7a 8a 9a 10a 11a 12p "
        "1p 2p 3p 4p 5p 6p 7p 8p 9p 10p 11p".split()
    )
    visual_color = [
        "#313695",
        "#4575b4",
        "#74add1",
        "#abd9e9",
        "#e0f3f8",
        "#ffffbf",
        "#fee090",
        "#fdae61",
        "#f46d43",
        "#d73027",
        "#a50026",
    ]
    months = ["{}月".format(i) for i in range(1, 13)]
    provinces = ["广东", "北京", "上海", "江西", "湖南", "浙江", "江苏"]
    guangdong_city = ["汕头市", "汕尾市", "揭阳市", "阳江市", "肇庆市", "广州市", "惠州市"]
    country = [
        "China",
        "Canada",
        "Brazil",
        "Russia",
        "United States",
        "Africa",
        "Germany",
    ]
    days_attrs = ["{}天".format(i) for i in range(30)]
    days_values = [random.randint(1, 30) for _ in range(30)]

    def choose(self) -> list:
        return random.choice(
            [
                self.clothes,
                self.drinks,
                self.phones,
                self.fruits,
                self.animal,
                self.dogs,
                self.week,
            ]
        )

    @staticmethod
    def values(start: int = 20, end: int = 150) -> list:
        return [random.randint(start, end) for _ in range(7)]

    @staticmethod
    def rand_color():
        return random.choice(
            [
                "#c23531",
                "#2f4554",
                "#61a0a8",
                "#d48265",
                "#749f83",
                "#ca8622",
                "#bda29a",
                "#6e7074",
                "#546570",
                "#c4ccd3",
                "#f05b72",
                "#444693",
                "#726930",
                "#b2d235",
                "#6d8346",
                "#ac6767",
                "#1d953f",
                "#6950a1",
            ]
        )

    @staticmethod
    def img_path(path: str, prefix: str = "images") -> str:
        return os.path.join(prefix, path)


Faker = _Faker()


class Collector:
    charts = []

    @staticmethod
    def funcs(fn):
        Collector.charts.append((fn, fn.__name__))


POPULATION = [
    ["Country (or dependency)", "Population\n(2019)"],
    ["China", 1420062022],
    ["India", 1368737513],
    ["United States", 329093110],
    ["Indonesia", 269536482],
    ["Brazil", 212392717],
    ["Pakistan", 204596442],
    ["Nigeria", 200962417],
    ["Bangladesh", 168065920],
    ["Russia", 143895551],
    ["Mexico", 132328035],
    ["Japan", 126854745],
    ["Ethiopia", 110135635],
    ["Philippines", 108106310],
    ["Egypt", 101168745],
    ["Vietnam", 97429061],
    ["DR Congo", 86727573],
    ["Turkey", 82961805],
    ["Iran", 82820766],
    ["Germany", 82438639],
    ["Thailand", 69306160],
    ["United Kingdom", 66959016],
    ["France", 65480710],
    ["Tanzania", 60913557],
    ["Italy", 59216525],
    ["South Africa", 58065097],
    ["Myanmar", 54336138],
    ["Kenya", 52214791],
    ["South Korea", 51339238],
    ["Colombia", 49849818],
    ["Spain", 46441049],
    ["Uganda", 45711874],
    ["Argentina", 45101781],
    ["Ukraine", 43795220],
    ["Algeria", 42679018],
    ["Sudan", 42514094],
    ["Iraq", 40412299],
    ["Poland", 38028278],
    ["Canada", 37279811],
    ["Afghanistan", 37209007],
    ["Morocco", 36635156],
    ["Saudi Arabia", 34140662],
    ["Peru", 32933835],
    ["Uzbekistan", 32807368],
    ["Venezuela", 32779868],
    ["Malaysia", 32454455],
    ["Angola", 31787566],
    ["Mozambique", 31408823],
    ["Ghana", 30096970],
    ["Nepal", 29942018],
    ["Yemen", 29579986],
    ["Madagascar", 26969642],
    ["North Korea", 25727408],
    ["Côte d'Ivoire", 25531083],
    ["Cameroon", 25312993],
    ["Australia", 25088636],
    ["Taiwan", 23758247],
    ["Niger", 23176691],
    ["Sri Lanka", 21018859],
    ["Burkina Faso", 20321560],
    ["Malawi", 19718743],
    ["Mali", 19689140],
    ["Romania", 19483360],
    ["Kazakhstan", 18592970],
    ["Syria", 18499181],
    ["Chile", 18336653],
    ["Zambia", 18137369],
    ["Guatemala", 17577842],
    ["Zimbabwe", 17297495],
    ["Netherlands", 17132908],
    ["Ecuador", 17100444],
    ["Senegal", 16743859],
    ["Cambodia", 16482646],
    ["Chad", 15814345],
    ["Somalia", 15636171],
    ["Guinea", 13398180],
    ["South Sudan", 13263184],
    ["Rwanda", 12794412],
    ["Benin", 11801595],
    ["Tunisia", 11783168],
    ["Burundi", 11575964],
    ["Belgium", 11562784],
    ["Cuba", 11492046],
    ["Bolivia", 11379861],
    ["Haiti", 11242856],
    ["Greece", 11124603],
    ["Dominican Republic", 10996774],
    ["Czechia", 10630589],
    ["Portugal", 10254666],
    ["Jordan", 10069794],
    ["Sweden", 10053135],
    ["Azerbaijan", 10014575],
    ["United Arab Emirates", 9682088],
    ["Hungary", 9655361],
    ["Honduras", 9568688],
    ["Belarus", 9433874],
    ["Tajikistan", 9292000],
    ["Austria", 8766201],
    ["Serbia", 8733407],
    ["Switzerland", 8608259],
    ["Papua New Guinea", 8586525],
    ["Israel", 8583916],
    ["Togo", 8186384],
    ["Sierra Leone", 7883123],
    ["Hong Kong", 7490776],
    ["Laos", 7064242],
    ["Bulgaria", 6988739],
    ["Paraguay", 6981981],
    ["Libya", 6569864],
    ["El Salvador", 6445405],
    ["Nicaragua", 6351157],
    ["Kyrgyzstan", 6218616],
    ["Lebanon", 6065922],
    ["Turkmenistan", 5942561],
    ["Singapore", 5868104],
    ["Denmark", 5775224],
    ["Finland", 5561389],
    ["Congo", 5542197],
    ["Slovakia", 5450987],
    ["Norway", 5400916],
    ["Eritrea", 5309659],
    ["State of Palestine", 5186790],
    ["Oman", 5001875],
    ["Costa Rica", 4999384],
    ["Liberia", 4977720],
    ["Ireland", 4847139],
    ["Central African Republic", 4825711],
    ["New Zealand", 4792409],
    ["Mauritania", 4661149],
    ["Kuwait", 4248974],
    ["Panama", 4226197],
    ["Croatia", 4140148],
    ["Moldova", 4029750],
    ["Georgia", 3904204],
    ["Puerto Rico", 3654978],
    ["Bosnia and Herzegovina", 3501774],
    ["Uruguay", 3482156],
    ["Mongolia", 3166244],
    ["Albania", 2938428],
    ["Armenia", 2936706],
    ["Jamaica", 2906339],
    ["Lithuania", 2864459],
    ["Qatar", 2743901],
    ["Namibia", 2641996],
    ["Botswana", 2374636],
    ["Lesotho", 2292682],
    ["Gambia", 2228075],
    ["Gabon", 2109099],
    ["North Macedonia", 2086720],
    ["Slovenia", 2081900],
    ["Guinea-Bissau", 1953723],
    ["Latvia", 1911108],
    ["Bahrain", 1637896],
    ["Swaziland", 1415414],
    ["Trinidad and Tobago", 1375443],
    ["Equatorial Guinea", 1360104],
    ["Timor-Leste", 1352360],
    ["Estonia", 1303798],
    ["Mauritius", 1271368],
    ["Cyprus", 1198427],
    ["Djibouti", 985690],
    ["Fiji", 918757],
    ["Réunion", 889918],
    ["Comoros", 850910],
    ["Bhutan", 826229],
    ["Guyana", 786508],
    ["Macao", 642090],
    ["Solomon Islands", 635254],
    ["Montenegro", 629355],
    ["Luxembourg", 596992],
    ["Western Sahara", 582478],
    ["Suriname", 573085],
    ["Cabo Verde", 560349],
    ["Micronesia", 536579],
    ["Maldives", 451738],
    ["Guadeloupe", 448798],
    ["Brunei", 439336],
    ["Malta", 433245],
    ["Bahamas", 403095],
    ["Belize", 390231],
    ["Martinique", 385320],
    ["Iceland", 340566],
    ["French Guiana", 296847],
    ["French Polynesia", 288506],
    ["Vanuatu", 288017],
    ["Barbados", 287010],
    ["New Caledonia", 283376],
    ["Mayotte", 266380],
    ["Sao Tome & Principe", 213379],
    ["Samoa", 198909],
    ["Saint Lucia", 180454],
    ["Guam", 167245],
    ["Channel Islands", 166828],
    ["Curaçao", 162547],
    ["Kiribati", 120428],
    ["St. Vincent & Grenadines", 110488],
    ["Tonga", 110041],
    ["Grenada", 108825],
    ["Aruba", 106053],
    ["U.S. Virgin Islands", 104909],
    ["Antigua and Barbuda", 104084],
    ["Seychelles", 95702],
    ["Isle of Man", 85369],
    ["Andorra", 77072],
    ["Dominica", 74679],
    ["Cayman Islands", 63129],
    ["Bermuda", 60833],
    ["Greenland", 56673],
    ["Saint Kitts & Nevis", 56345],
    ["American Samoa", 55727],
    ["Northern Mariana Islands", 55246],
    ["Marshall Islands", 53211],
    ["Faeroe Islands", 49692],
    ["Sint Maarten", 40939],
    ["Monaco", 39102],
    ["Liechtenstein", 38404],
    ["Turks and Caicos", 36461],
    ["Gibraltar", 34879],
    ["San Marino", 33683],
    ["British Virgin Islands", 32206],
    ["Caribbean Netherlands", 25971],
    ["Palau", 22206],
    ["Cook Islands", 17462],
    ["Anguilla", 15174],
    ["Wallis & Futuna", 11617],
    ["Tuvalu", 11393],
    ["Nauru", 11260],
    ["Saint Pierre & Miquelon", 6375],
    ["Montserrat", 5220],
    ["Saint Helena", 4096],
    ["Falkland Islands", 2921],
    ["Niue", 1628],
    ["Tokelau", 1340],
    ["Holy See", 799],
]
