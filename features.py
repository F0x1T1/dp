
features_list = [
    'MSSubClass',
    'MSZoning',
    'LotFrontage',
    'LotArea',
    'Street',
    'Alley',
    'LotShape',
    'LandContour',
    'Utilities',
    'LotConfig',
    'LandSlope',
    'Neighborhood',
    'Condition1',
    'Condition2',
    'BldgType',
    'HouseStyle',
    'OverallQual',
    'OverallCond',
    'YearBuilt',
    'YearRemodAdd',
    'RoofStyle',
    'RoofMatl',
    'Exterior1st',
    'Exterior2nd',
    'MasVnrType',
    'MasVnrArea',
    'ExterQual',
    'ExterCond',
    'Foundation',
    'BsmtQual',
    'BsmtCond',
    'BsmtExposure',
    'BsmtFinType1',
    'BsmtFinSF1',
    'BsmtFinType2',
    'BsmtFinSF2',
    'BsmtUnfSF',
    'TotalBsmtSF',
    'Heating',
    'HeatingQC',
    'CentralAir',
    'Electrical',
    '1stFlrSF',
    '2ndFlrSF',
    'LowQualFinSF',
    'GrLivArea',
    'BsmtFullBath',
    'BsmtHalfBath',
    'FullBath',
    'HalfBath',
    'Bedroom',
    'Kitchen',
    'KitchenQual',
    'TotRmsAbvGrd',
    'Functional',
    'Fireplaces',
    'FireplaceQu',
    'GarageType',
    'GarageYrBlt',
    'GarageFinish',
    'GarageCars',
    'GarageArea',
    'GarageQual',
    'GarageCond',
    'PavedDrive',
    'WoodDeckSF',
    'OpenPorchSF',
    'EnclosedPorch',
    '3SsnPorch',
    'ScreenPorch',
    'PoolArea',
    'PoolQC',
    'Fence',
    'MiscFeature',
    'MiscVal',
    'MoSold',
    'YrSold',
    'SaleType',
    'SaleCondition',
]


feature_form_structure = {
    'Загальне': [
        {
            'Label': 'MSSubClass',
            'Data' :  {
                'Description': 'Ідентифікує тип житла, що бере участь у продажу.',
                'Form': {
                    '20': '1-ПОВЕРХОВІ 1946 ТА НОВІШІ ВСІ СТИЛІ',
                    '30': '1-ПОВЕРХОВІ 1945 РОКУ І СТАРІШІ',
                    '40': '1-ПОВЕРХОВІ З МАНСАРДОЮ ВСІХ РОКІВ',
                    '45': '1-1/2-ПОВЕРХОВІ - НЕДОБУДОВАНІ, БУДЬ-ЯКОГО ВІКУ',
                    '50': '1-1/2-ПОВЕРХОВІ НЕДОБУДОВАНІ БУДЬ-ЯКОГО ВІКУ',
                    '60': '2-ПОВЕРХОВІ 1946 РОКУ ТА НОВІШІ',
                    '70': '2-ПОВЕРХОВІ 1945 РОКУ І СТАРШІ',
                    '75': '2-1/2-ПОВЕРХОВІ, БУДЬ-ЯКОГО ВІКУ',
                    '80': 'ДВОРІВНЕВІ АБО БАГАТОРІВНЕВІ',
                    '85': 'РОЗДІЛЬНЕ ФОЙЄ',
                    '90': 'ДВОРІВНЕВІ - ВСІ СТИЛІ ТА ВІКОВІ КАТЕГОРІЇ',
                    '120': '1-поверховий ПЗБ (планова забудова) - 1946 р. і новіше',
                    '150': '1-1/2-ПОВЕРХОВИЙ ПУД - БУДЬ-ЯКОГО ВІКУ',
                    '160': '2-ПОВЕРХОВИЙ ПУД - 1946 І НОВІШЕ',
                    '180': 'ПУД - БАГАТОРІВНЕВИЙ - В Т.Ч. РОЗДІЛЬНИЙ ПОВЕРХ/ФОЙЄ',
                    '190': 'ПЕРЕПЛАНУВАННЯ НА 2 СІМЇ - ВСІ СТИЛІ ТА ЕПОХИ',
                }
            }
        },
        {
            'Label': 'MSZoning',
            'Data' :  {
                'Description': 'Визначає загальну зональну класифікацію продажу.',
                'Form': {
                    'A':	'Сільське господарство',
                    'C':	'Комерція',
                    'FV':	'Плавуче житлове селище',
                    'I':	'Промисловість',
                    'RH':	'Висока щільність житлової забудови',
                    'RL':	'Низька щільність житлової забудови',
                    'RP':	'Парк житлової низької щільності ',
                    'RM':	'Житлова середня щільність',
                }
            }
        },
        {
            'Label': 'LotFrontage',
            'Data' :  {
                'Description': 'Лінійні метри вулиці, зєднаної з обєктом нерухомості',
                'Form': 'float64',
            }
        },
        {
            'Label': 'LotArea',
            'Data' :  {
                'Description': 'Розмір лоту в квадратних метрах',
                'Form': 'float64'
            },
        },
        {
            'Label': 'Street',
            'Data' :  {
                'Description': 'Тип підїзду до обєкта нерухомості',
                'Form': {
                    'Grvl':	'Гравій',
                    'Pave':	'Асфальтовано',
                }
            },
        },
        {
            'Label': 'Alley',
            'Data' :  {
                'Description': 'Тип алеї що прилягає до обєкту нерухомості',
                'Form': {
                    'Grvl':	'Гравій',
                    'Pave':	'Асфальтовано',
                    'NA': 	'Без алеї',
                }
            }
        },
        {
            'Label': 'LotShape',
            'Data' :  {
                'Description': 'Загальна форма власності',
                'Form': {
                    'Reg':	'Звичайний',
                    'IR1':	'Трохи неофіційна',
                    'IR2':	'Помірно неофіційна',
                    'IR3':	'Неофіційна',
                }
            }
        },
        {
            'Label': 'LandContour',
            'Data' :  {
                'Description': 'Рівність обєкта нерухомості',
                'Form': {
                    'Lvl':	'Майже плоский/рівневий',
                    'Bnk':	'Набережний – швидкий і значний підйом від рівня вулиці до будівлі',
                    'HLS':	'Схил пагорба – значний нахил з боку в бік',
                    'Low':	'На схилі',
                },
            }
        },
        {
            'Label': 'Utilities',
            'Data' :  {
                'Description': 'Тип наявних комунальних послуг',
                'Form': {
                    'AllPub':	'Всі комунальні послуги',
                    'NoSewr':	'Електрика, газ, вода ',
                    'NoSeWa':	'Тільки електрика та газ',
                    'ELO':	'Тільки електрика',
                }
            }
        },
        {
            'Label': 'LotConfig',
            'Data' :  {
                'Description': 'Конфігурація',
                'Form': {
                    'Inside':	'Внутрішній бік',
                    'Corner':	'Кутова ділянка',
                    'CulDSac':	'глухий провулок',
                    'FR2':	'Фасад на 2 сторони ділянки',
                    'FR3':	'Фасад на 3 сторони ділянки',
                }
            }
        },
        {
            'Label': 'LandSlope',
            'Data' :  {
                'Description': 'Схил власності',
                'Form': {
                    'Gtl':	'Пологий схил',
                    'Mod':	'Помірний нахил	',
                    'Sev':	'Сильний схил',
                }
            }
        },
        {
            'Label': 'Neighborhood',
            'Data' :  {
                'Description': 'Фізичні місцезнаходження в межах міста',
                'Form': {
                    'Blmngtn':	'Bloomington Heights',
                    'Blueste':	'Bluestem',
                    'BrDale':	'Briardale',
                    'BrkSide':	'Brookside',
                    'ClearCr':	'Clear Creek',
                    'CollgCr':	'College Creek',
                    'Crawfor':	'Crawford',
                    'Edwards':	'Edwards',
                    'Gilbert':	'Gilbert',
                    'IDOTRR':	'Iowa DOT and Rail Road',
                    'MeadowV':	'Meadow Village',
                    'Mitchel':	'Mitchell',
                    'Names':	'North Ames',
                    'NoRidge':	'Northridge',
                    'NPkVill':	'Northpark Villa',
                    'NridgHt':	'Northridge Heights',
                    'NWAmes':	'Northwest Ames',
                    'OldTown':	'Old Town',
                    'SWISU':	'South & West of Iowa State University',
                    'Sawyer':	'Sawyer',
                    'SawyerW':	'Sawyer West',
                    'Somerst':	'Somerset',
                    'StoneBr':	'Stone Brook',
                    'Timber':	'Timberland',
                    'Veenker':	'Veenker',
                }
            }
        },
        {
            'Label': 'Condition1',
            'Data' :  {
                'Description': 'Близькість до різних умов',
                'Form': {
                    'Artery':	'Примикає до магістральної дороги',
                    'Feedr':	'Примикає до підїзної дороги',
                    'Norm':	'Normal	',
                    'RRNn':	"В межах 200м від залізниці",
                    'RRAn':	'Примикає до залізниці ',
                    'PosN':	'Поруч позитивна особливість за межами майданчика - парк, зелена зона і т.д.',
                    'PosA':	'Adjacent to postive off-site feature',
                    'RRNe':	"В межах 200' від залізниці Схід-Захід",
                    'RRAe':	'Примикає до залізниці Схід-Захід',
                }
            }
        },
        {
            'Label': 'Condition2',
            'Data' :  {
                'Description': 'Близькість до різних умов (якщо їх декілька)',
                'Form': {
                    'Artery':	'Adjacent to arterial street',
                    'Feedr':	'Adjacent to feeder street',
                    'Norm':	'Normal	',
                    'RRNn':	"Within 200' of North-South Railroad",
                    'RRAn':	'Adjacent to North-South Railroad',
                    'PosN':	'Near positive off-site feature--park, greenbelt, etc.',
                    'PosA':	'Adjacent to postive off-site feature',
                    'RRNe':	"Within 200' of East-West Railroad",
                    'RRAe':	'Adjacent to East-West Railroad',
                }
            }
        },
        {
            'Label': 'Functional',
            'Data' :  {
                'Description': 'Домашня функціональність (Вважається типовою, якщо немає підстав для відрахувань)',
                'Form': {
                    'Typ':	'Typical Functionality',
                    'Min1':	'Minor Deductions 1',
                    'Min2':	'Minor Deductions 2',
                    'Mod':	'Moderate Deductions',
                    'Maj1':	'Major Deductions 1',
                    'Maj2':	'Major Deductions 2',
                    'Sev':	'Severely Damaged',
                    'Sal':	'Salvage only',
                }
            }
        },
    ],
    'Характеристики споруди': [
        {
            'Label': 'BldgType',
            'Data' :  {
                'Description': 'Тип житла',
                'Form': {
                    '1Fam':	'Single-family Detached	',
                    '2FmCon':	'Two-family Conversion; originally built as one-family dwelling',
                    'Duplx':	'Duplex',
                    'TwnhsE':	'Townhouse End Unit',
                    'TwnhsI':	'Townhouse Inside Unit',
                }
            }
        },
        {
            'Label': 'HouseStyle',
            'Data' :  {
                'Description': 'Кількість поверхів',
                'Form': {
                    '1Story':	'Одноповерховий',
                    '1.5Fin':	'One and one-half story: 2nd level finished',
                    '1.5Unf':	'One and one-half story: 2nd level unfinished',
                    '2Story':	'Two story',
                    '2.5Fin':	'Two and one-half story: 2nd level finished',
                    '2.5Unf':	'Two and one-half story: 2nd level unfinished',
                    'SFoyer':	'Split Foyer',
                    'SLvl':	'Split Level',
                }
            }
        },
        {
            'Label': 'OverallQual',
            'Data' :  {
                'Description': 'Оцінює загальний матеріал та оздоблення будинку',
                'Form': {
                    '10':	'Very Excellent',
                    '9':	'Excellent',
                    '8':	'Very Good',
                    '7':	'Good',
                    '6':	'Above Average',
                    '5':	'Average',
                    '4':	'Below Average',
                    '3':	'Fair',
                    '2':	'Poor',
                    '1':	'Very Poor',
                }
            }
        },
        {
            'Label': 'OverallCond',
            'Data' :  {
                'Description': 'Оцінка загального стану будинку',
                'Form': {
                    '10':	'Very Excellent',
                    '9':	'Excellent',
                    '8':	'Very Good',
                    '7':	'Good',
                    '6':	'Above Average',
                    '5':	'Average',
                    '4':	'Below Average',
                    '3':	'Fair',
                    '2':	'Poor',
                    '1':	'Very Poor',
                }
            }
        },
        {
            'Label': 'OverallCond',
            'Data' :  {
                'Description': 'Рік побудови будинка',
                'Form': 'int64',
            }
        },
        {
            'Label': 'YearRemodAdd',
            'Data' :  {
                'Description': 'Дата реконструкції (збігається з датою будівництва, якщо не було реконструкції)',
                'Form': 'int64',
            }
        },
        {
            'Label': 'RoofStyle',
            'Data' :  {
                'Description': 'Тип даху',
                'Form': {
                    'Flat':	'Flat',
                    'Gable':	'Gable',
                    'Gambrel':	'Gabrel (Barn)',
                    'Hip':	'Hip',
                    'Mansard':	'Mansard',
                    'Shed':	'Shed',
                },
            }
        },
        {
            'Label': 'RoofMatl',
            'Data' :  {
                'Description': 'Покрівельний матеріал',
                'Form': {
                    'ClyTile':	'Clay or Tile',
                    'CompShg':	'Standard (Composite) Shingle',
                    'Membran':	'Membrane',
                    'Metal':	'Metal',
                    'Roll':	'Roll',
                    'Tar&Grv':	'Gravel & Tar',
                    'WdShake':	'Wood Shakes',
                    'WdShngl':	'Wood Shingles',

                }
            }
        },
        {
            'Label': 'Exterior1st',
            'Data' :  {
                'Description': 'Зовнішнє покриття будинку',
                'Form': {
                    'AsbShng':	'Asbestos Shingles',
                    'AsphShn':	'Asphalt Shingles',
                    'BrkComm':	'Brick Common',
                    'BrkFace':	'Brick Face',
                    'CBlock':	'Cinder Block',
                    'CemntBd':	'Cement Board',
                    'HdBoard':	'Hard Board',
                    'ImStucc':	'Imitation Stucco',
                    'MetalSd':	'Metal Siding',
                    'Other':	'Other',
                    'Plywood':	'Plywood',
                    'PreCast':	'PreCast	',
                    'Stone':	'Stone',
                    'Stucco':	'Stucco',
                    'VinylSd':	'Vinyl Siding',
                    'WdSdng': 'Wood Siding',
                    'WdShing':	'Wood Shingles',
                }
            }
        },
        {
            'Label': 'Exterior2nd',
            'Data' :  {
                'Description': 'Зовнішнє покриття будинку (якщо більше одного матеріалу)',
                'Form': {
                    'AsbShng':	'Asbestos Shingles',
                    'AsphShn':	'Asphalt Shingles',
                    'BrkComm':	'Brick Common',
                    'BrkFace':	'Brick Face',
                    'CBlock':	'Cinder Block',
                    'CemntBd':	'Cement Board',
                    'HdBoard':	'Hard Board',
                    'ImStucc':	'Imitation Stucco',
                    'MetalSd':	'Metal Siding',
                    'Other':	'Other',
                    'Plywood':	'Plywood',
                    'PreCast':	'PreCast	',
                    'Stone':	'Stone',
                    'Stucco':	'Stucco',
                    'VinylSd':	'Vinyl Siding',
                    'WdSdng': 'Wood Siding',
                    'WdShing':	'Wood Shingles',
                }
            }
        },
        {
            'Label': 'MasVnrType',
            'Data' :  {
                'Description': 'Тип кладки шпону',
                'Form': {
                    'BrkCmn':	'Brick Common',
                    'BrkFace':	'Brick Face',
                    'CBlock':	'Cinder Block',
                    'None':	'None',
                    'Stone':	'Stone',
                }
            }
        },
        {
            'Label': 'MasVnrArea',
            'Data' :  {
                'Description': 'Площа кладки шпону в квадратних футах',
                'Form': 'float64',
            }
        },
        {
            'Label': 'ExterQual',
            'Data' : {
                'Description': 'Оцінює якість матеріалу на зовнішній стороні',
                'Form': {
                    'Ex':	'Excellent',
                    'Gd':	'Good',
                    'TA':	'Average/Typical',
                    'Fa':	'Fair',
                    'Po':	'Poor',
                }
            }
        },
        {
            'Label': 'ExterCond',
            'Data' : {
                'Description': 'Оцінює поточний стан матеріалу на зовнішній стороні',
                'Form': {
                    'Ex':	'Excellent',
                    'Gd':	'Good',
                    'TA':	'Average/Typical',
                    'Fa':	'Fair',
                    'Po':	'Poor',
                }
            }
        },
        {
            'Label': 'Foundation',
            'Data' : {
                'Description': 'Тип фундаменту',
                'Form': {
                    'BrkTil':	'Brick & Tile',
                    'CBlock':	'Cinder Block',
                    'PConc':	'Poured Contrete	',
                    'Slab':	'Slab',
                    'Stone':	'Stone',
                    'Wood':	'Wood',
                }
            }
        },
        {
            'Label': '1stFlrSF',
            'Data' : {
                'Description': 'Перший поверх квадратних футів',
                'Form': 'float64',
            }
        },
        {
            'Label': '2ndFlrSF',
            'Data' : {
                'Description': 'Другий поверх, квадратні фути',
                'Form': 'float64',
            }
        },
        {
            'Label': 'LowQualFinSF',
            'Data' : {
                'Description': 'Нижній поріг готових квадратних метрів (всі поверхи)',
                'Form': 'float64',
            }
        },
        {
            'Label': 'GrLivArea',
            'Data' : {
                'Description': 'Житлова площа над рівнем землі квадратних футів',
                'Form': 'float64',
            }
        },
    ],
    'Підвал': [
        {
            'Label': 'BsmtQual',
            'Data' : {
                'Description': 'Висоту підвалу',
                'Form': {
                    'Ex':	'Excellent (100+ inches)',
                    'Gd':	'Good (90-99 inches)',
                    'TA':	'Typical (80-89 inches)',
                    'Fa':	'Fair (70-79 inches)',
                    'Po':	'Poor (<70 inches',
                    'NA':	'No Basement',
                }
            }
        },
        {
            'Label': 'BsmtCond',
            'Data' : {
                'Description': 'загальний стан підвалу',
                'Form': {
                    'Ex':	'Excellent',
                    'Gd':	'Good',
                    'TA':	'Typical - slight dampness allowed',
                    'Fa':	'Fair - dampness or some cracking or settling',
                    'Po':	'Poor - Severe cracking, settling, or wetness',
                    'NA':	'No Basement',
                }
            }
        },
        {
            'Label': 'BsmtExposure',
            'Data' : {
                'Description': 'Відноситься до стін на рівні виходу або саду',
                'Form': {
                    'Gd':	'Good Exposure',
                    'Av':	'Average Exposure (split levels or foyers typically score average or above)	',
                    'Mn':	'Mimimum Exposure',
                    'No':	'No Exposure',
                    'NA':	'No Basement',
                }
            }
        },
        {
            'Label': 'BsmtFinType1',
            'Data' : {
                'Description': 'Стан готової площі підвалу',
                'Form': {
                    'GLQ':	'Good Living Quarters',
                    'ALQ':	'Average Living Quarters',
                    'BLQ':	'Below Average Living Quarters	',
                    'Rec':	'Average Rec Room',
                    'LwQ':	'Low Quality',
                    'Unf':	'Unfinshed',
                    'NA':	'No Basement',
                }
            }
        },
        {
            'Label': 'BsmtFinSF1',
            'Data' : {
                'Description': 'Готові квадратні метри типу 1',
                'Form': 'float64',
            }
        },
        {
            'Label': 'BsmtFinType2',
            'Data' : {
                'Description': 'Оцінка площі обробленого підвалу (якщо декілька типів)',
                'Form': {
                    'GLQ':	'Good Living Quarters',
                    'ALQ':	'Average Living Quarters',
                    'BLQ':	'Below Average Living Quarters	',
                    'Rec':	'Average Rec Room',
                    'LwQ':	'Low Quality',
                    'Unf':	'Unfinshed',
                    'NA':	'No Basement',
                }
            }
        },
        {
            'Label': 'BsmtFinSF2',
            'Data' : {
                'Description': 'Готові квадратні метри типу 2',
                'Form': 'float64',
            }
        },
        {
            'Label': 'BsmtUnfSF',
            'Data' : {
                'Description': 'Unfinished square feet of basement area',
                'Form': 'float64',
            }
        },
        {
            'Label': 'TotalBsmtSF',
            'Data' : {
                'Description': 'Total square feet of basement area',
                'Form': 'float64',
            }
        },
    ],
    'Утиліти': [
        {
            'Label': 'Heating',
            'Data' : {
                'Description': 'Type of heating',
                'Form': {
                    'Floor':	'Floor Furnace',
                    'GasA':	'Gas forced warm air furnace',
                    'GasW':	'Gas hot water or steam heat',
                    'Grav':	'Gravity furnace	',
                    'OthW':	'Hot water or steam heat other than gas',
                    'Wall':	'Wall furnace  ',
                },
            }
        },
        {
            'Label': 'HeatingQC',
            'Data' : {
                'Description': 'Heating quality and condition',
                'Form': {
                    'Ex':	'Excellent',
                    'Gd':	'Good',
                    'TA':	'Average/Typical',
                    'Fa':	'Fair',
                    'Po':	'Poor',
                },
            }
        },
        {
            'Label': 'CentralAir',
            'Data' : {
                'Description': 'Central air conditioning',
                'Form': {
                    'N':	'No',
                    'Y':	'Yes',
                },
            }
        },
        {
            'Label': 'Electrical',
            'Data' : {
                'Description': 'Electrical system',
                'Form': {
                    'SBrkr':	'Standard Circuit Breakers & Romex',
                    'FuseA':	'Fuse Box over 60 AMP and all Romex wiring (Average)	',
                    'FuseF':	'60 AMP Fuse Box and mostly Romex wiring (Fair)',
                    'FuseP':	'60 AMP Fuse Box and mostly knob & tube wiring (poor)',
                    'Mix':	'Mixed',
                },
            }
        },
    ],
    'Ванна кімната': [
        {
            'Label': 'BsmtFullBath',
            'Data' : {
                'Description': 'Basement full bathrooms',
                'Form': 'float64',
            }
        },
        {
            'Label': 'BsmtHalfBath',
            'Data' : {
                'Description': 'Basement half bathrooms',
                'Form': 'float64',
            }
        },
        {
            'Label': 'FullBath',
            'Data' : {
                'Description': 'Full bathrooms above grade',
                'Form': 'float64',
            }
        },
        {
            'Label': 'HalfBath',
            'Data' : {
                'Description': 'Half baths above grade',
                'Form': 'float64',
            }
        },
    ],
    'Спальня': [
        {
            'Label': 'Bedroom',
            'Data' : {
                'Description': 'Bedrooms above grade (does NOT include basement bedrooms)',
                'Form': 'int64'
            }
        }
    ],
    'Кухня': [
        {
            'Label': 'Kitchen',
            'Data' : {
                'Description': 'Kitchens above grade',
                'Form': 'int64',
            }
        },
        {
            'Label': 'KitchenQual',
            'Data' : {
                'Description': 'Kitchen quality',
                'Form': {
                    'Ex':	'Excellent',
                    'Gd':	'Good',
                    'TA':	'Typical/Average',
                    'Fa':	'Fair',
                    'Po':	'Poor  ',
                },
            }
        },
    ],
    'Гараж': [
        {
            'Label': 'GarageType',
            'Data' : {
                'Description': 'Garage location',
                'Form': {
                    '2Types':	'More than one type of garage',
                    'Attchd':	'Attached to home',
                    'Basment':	'Basement Garage',
                    'BuiltIn':	'Built-In (Garage part of house - typically has room above garage)',
                    'CarPort':	'Car Port',
                    'Detchd':	'Detached from home',
                    'NA':	'No Garage',
                },
            }
        },
        {
            'Label': 'GarageYrBlt',
            'Data' : {
                'Description': 'Year garage was built',
                'Form': 'int64'
            }
        },
        {
            'Label': 'GarageFinish',
            'Data' : {
                'Description': 'Interior finish of the garage',
                'Form': {
                    'Fin':	'Finished',
                    'RFn':	'Rough Finished	',
                    'Unf':	'Unfinished',
                    'NA':	'No Garage',
                }
            }
        },
        {
            'Label': 'GarageCars',
            'Data' : {
                'Description': 'Size of garage in car capacity',
                'Form': 'int64'
            }
        },
        {
            'Label': 'GarageArea',
            'Data' : {
                'Description': 'Size of garage in square feet',
                'Form': 'float64'
            }
        },
        {
            'Label': 'GarageQual',
            'Data' : {
                'Description': 'Garage quality',
                'Form': {
                    'Ex':	'Excellent',
                    'Gd':	'Good',
                    'TA':	'Typical/Average',
                    'Fa':	'Fair',
                    'Po':	'Poor',
                    'NA':	'No Garage',
                }
            }
        },
        {
            'Label': 'GarageCond',
            'Data' : {
                'Description': 'Garage condition',
                'Form': {
                    'Ex':	'Excellent',
                    'Gd':	'Good',
                    'TA':	'Typical/Average',
                    'Fa':	'Fair',
                    'Po':	'Poor',
                    'NA':	'No Garage',
                }
            }
        },
    ],
    'Інші': [
        {
            'Label': 'TotRmsAbvGrd',
            'Data' : {
                'Description': 'Total rooms above grade (does not include bathrooms)',
                'Form': 'int64',
            }
        },
        {
            'Label': 'Fireplaces',
            'Data' : {
                'Description': 'Number of fireplaces',
                'Form': 'int64',
            }
        },
        {
            'Label': 'FireplaceQu',
            'Data' : {
                'Description': 'Fireplace quality',
                'Form': {
                    'Ex':	'Excellent - Exceptional Masonry Fireplace',
                    'Gd':	'Good - Masonry Fireplace in main level',
                    'TA':	'Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement',
                    'Fa':	'Fair - Prefabricated Fireplace in basement',
                    'Po':	'Poor - Ben Franklin Stove',
                    'NA':	'No Fireplace',
                },
            }
        },
        {
            'Label': 'PavedDrive',
            'Data' : {
                'Description': 'Paved driveway',
                'Form': {
                    'Y':	'Paved',
                    'P':	'Partial Pavement',
                    'N':	'Dirt/Gravel',
                }
            }
        },
        {
            'Label': 'WoodDeckSF',
            'Data' : {
                'Description': 'Wood deck area in square feet',
                'Form': 'float64',
            }
        },
        {
            'Label': 'OpenPorchSF',
            'Data' : {
                'Description': 'Open porch area in square feet',
                'Form': 'float64',
            }
        },
        {
            'Label': 'EnclosedPorch',
            'Data' : {
                'Description': 'Enclosed porch area in square feet',
                'Form': 'float64',
            }
        },
        {
            'Label': '3SsnPorch',
            'Data' : {
                'Description': 'Площа всесезонного ганку в квадратних футах',
                'Form': 'float64',
            }
        },
        {
            'Label': 'ScreenPorch',
            'Data' : {
                'Description': 'Площа ґанку в квадратних футах',
                'Form': 'float64',
            }
        },
        {
            'Label': 'PoolArea',
            'Data' : {
                'Description': 'Площа басейну в квадратних футах',
                'Form': 'float64',
            }
        },
        {
            'Label': 'PoolQC',
            'Data' : {
                'Description': 'Якість басейну',
                'Form': {
                    'Ex':	'Чудовий',
                    'Gd':	'Добрий',
                    'TA':	'Average/Typical',
                    'Fa':	'Справедливо',
                    'NA':	'Без басейну',
                },
            }
        },
        {
            'Label': 'Fence',
            'Data' : {
                'Description': 'Якість огорожі',
                'Form': {
                    'GdPrv':	'Висока',
                    'MnPrv':	'Низька',
                    'GdWo':	'Добра деревина.',
                    'MnWw':	'Minimum Wood/Wire',
                    'NA':	'No Fence',
                },
            }
        },
        {
            'Label': 'MiscFeature',
            'Data' : {
                'Description': 'Різні функції, які не охоплені іншими категоріями',
                'Form': {
                    'Elev':	'Ліфт',
                    'Gar2':	'2-й гараж. (якщо не описано в розділі Гараж)',
                    'Othr':	'Інше',
                    'Shed':	'Shed (over 100 SF)',
                    'TenC':	'Тенісний корт',
                    'NA':	'None  ',
                },
            }
        },
        #{
         #   'Label': 'MiscVal',
          #  'Data' : {
           #     'Description': 'Значення різних конфігурацій',
            #    'Form': 'float64',
           # }
        #},
              #{
          #  'Label': 'MoSold',
            #'Data' : {
              #  'Description': 'Month Sold (MM)',
              #'Form': 'int64',
           # }
        #},
        #{
        #    'Label': 'YrSold',
         #   'Data' : {
          #      'Description': 'Рік продажу (YYYY)',
           #     'Form': 'int64',
           # }
       # },
        {
            'Label': 'SaleType',
            'Data' : {
                'Description': 'Тип продажу',
                'Form': {
                    'WD': 	'Гарантійний лист - звичайний',
                    'CWD':	'Гарантійний лист - готівка',
                    'VWD':	'Гарантійний акт - Іпотека',
                    'New':	'Будинок щойно збудований та проданий - новобудова',
                    'COD':	'Акт судового службовця/майно',
                    'Con':	'Договір 15% початковий внесок на звичайних умовах',
                    'ConLw':	'Контракт Низький початковий внесок і низькі відсотки',
                    'ConLI':	'Контракт з низькими відсотками',
                    'ConLD':	'Контракт Low Down',
                    'Oth':	'Інші',
                },
            }
        },
        {
            'Label': 'SaleCondition',
            'Data' : {
                'Description': 'Умова продажу',
                'Form': {
                    'Normal':	'Звичайний продаж',
                    'Abnorml':	'Ненормальний продаж - торгівля, викуп, короткий продаж',
                    'AdjLand':	'Купівля прилеглої землі',
                    'Alloca':	'Розподіл – два пов’язані об’єкти нерухомості з окремими документами, як правило, квартира з гаражем',
                    'Family':	'Продаж між членами сімї',
                    'Partial':	'Будинок не був завершений під час останньої оцінки',
                },
            }
        },
    ],
}
