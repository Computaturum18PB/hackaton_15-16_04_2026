# Заметки - справочник функций библиотеки RDKit

## Создание и конвертация молекул

- `Chem.MolFromSmiles('CCO')` - создание молекулы из SMILES строки;
- `Chem.MolToSmiles(mol)` - преобразование молекулы в SMILES (каноническая форма);
- `Chem.MolFromSmarts('[CH3]')` - создание паттерна из SMARTS для поиска;
- `Chem.MolToMolBlock(mol)` - преобразование в MDL Mol блок;
- `Chem.MolFromMolFile('file.mol')` - загрузка из MOL файла;


```
Базовые символы
C	Атом углерода
O	Атом кислорода
N	Атом азота	
=	Двойная связь	
#	Тройная связь
.	Разделитель молекул
()	Ветвление
C1CCCCC1 - циклогексан
c1ccccc1 - бензол (ароматический)
C1=CC=CC=C1 - бензол (альтернативный)
O1CCOCC1 - 1,4-диоксан
c - ароматический C
n - ароматический N
o - ароматический O
s - ароматический S
C(CC)(CC)CC   - неопентан
CC(O)C(=O)O   - молочная кислота
@	Античасовой (CCW)
@@	Часовой (CW)
/	Транс-связь (E)
\	Цис-связь (Z)
C[C@H](O)C(=O)O   - L-молочная (R)
C[C@@H](O)C(=O)O  - D-молочная (S)
F/C=C/F           - транс- (E)
F/C=C\F           - цис- (Z)
[Na+]     - ион натрия
[OH-]     - гидроксид
[NH4+]    - аммоний
[13C]     - углерод-13
[2H]      - дейтерий
```

## Загрузка и сохранение данных

- `Chem.SDMolSupplier('file.sdf')` - чтение SDF файла с молекулами;
- `Chem.SDWriter('output.sdf')` - запись молекул в SDF файл;
- `PandasTools.AddMoleculeColumnToFrame(df, 'SMILES', 'Molecule')` - добавление колонки с молекулами в DataFrame;
- `PandasTools.SaveXlsxFromFrame(df, 'file.xlsx')` - сохранение DataFrame с изображениями молекул в Excel;

## Визуализация

- `Draw.MolToImage(mol)` - создание изображения молекулы;
- `Draw.MolsToGridImage(mols, molsPerRow=3)` - сетка изображений нескольких молекул;
- `Draw.ReactionToImage(rxn)` - визуализация химической реакции;

## Атрибуты молекулы

- `mol.GetNumAtoms()` - количество атомов;
- `mol.GetNumBonds()` - количество связей;
- `mol.GetAtoms()` - итератор по атомам;
- `mol.GetBonds()` - итератор по связям;
- `mol.GetRingInfo()` - информация о кольцах;
- `mol.GetSubstructMatches(pattern)` - поиск всех совпадений с паттерном;

## Работа с атомами

- `atom.GetSymbol()` - символ атома;
- `atom.GetAtomicNum()` - атомный номер;
- `atom.GetDegree()` - количество связей;
- `atom.GetHybridization()` - тип гибридизации;
- `atom.GetIdx()` - индекс атома;
- `atom.GetIsAromatic()` - проверка на ароматичность (True/False);

## Работа со связями

- `bond.GetBondType()` - тип связи;
- `bond.GetBeginAtomIdx()` - индекс начального атома;
- `bond.GetEndAtomIdx()` - индекс конечного атома;
- `bond.GetIsConjugated()` - проверка на сопряженность;
- `bond.GetIsInRing()` - проверка на вхождение в кольцо;

## Модификация молекул

- `Chem.RemoveHs(mol)` - удаление явных атомов водорода;
- `Chem.AddHs(mol)` - добавление явных атомов водорода;
- `Chem.SanitizeMol(mol)` - санитизация (проверка валентностей и связей);
- `Chem.AssignStereochemistry(mol)` - назначение стереохимии;
- `Chem.RWMol(mol)` - создание редактируемой копии молекулы;

## Дескрипторы (физико-химические свойства)

- `Descriptors.MolWt(mol)` - молекулярная масса;
- `Descriptors.MolLogP(mol)` - липофильность (logP);
- `Descriptors.NumHAcceptors(mol)` - количество акцепторов водородной связи;
- `Descriptors.NumHDonors(mol)` - количество доноров водородной связи;
- `Descriptors.TPSA(mol)` - топологическая полярная поверхность;
- `Descriptors.NumRotatableBonds(mol)` - количество вращаемых связей;
- `rdMolDescriptors.CalcMolFormula(mol)` - молекулярная формула;

## Фингерпринты (для поиска схожести)

- `AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)` - Morgan фингерпринт (ECFP);
- `MACCSkeys.GenMACCSKeys(mol)` - MACCS ключи (166 бит);
- `RDKFingerprint(mol)` - стандартный RDKit фингерпринт;
- `DataStructs.TanimotoSimilarity(fp1, fp2)` - Tanimoto коэффициент схожести;

## Поиск и фильтрация

- `mol.HasSubstructMatch(pattern)` - проверка наличия подструктуры;
- `mol.GetSubstructMatch(pattern)` - индексы атомов первого совпадения;
- `mol.GetSubstructMatches(pattern)` - индексы всех совпадений;
- `Chem.ReplaceSubstructs(mol, pattern, replacement)` - замена подструктуры;
- `SaltRemover.SaltRemover().StripMol(mol)` - удаление солей (оставить основную структуру);

## Очистка и нормализация

- `.dropna()` - удаление строк с пропусками;
- `.fillna(значение)` - заполнение пропусков указанным значением;

## Агрегация и группировка

- `Chem.rdMolDescriptors.CalcNumAromaticRings(mol)` - количество ароматических колец;
- `Chem.rdMolDescriptors.CalcNumAliphaticRings(mol)` - количество алифатических колец;
- `Chem.rdMolDescriptors.CalcNumSaturatedRings(mol)` - количество насыщенных колец;
- `Chem.Lipinski.NumHBD(mol)` - количество доноров H-связи (правило Липински);
- `Chem.Lipinski.NumHBA(mol)` - количество акцепторов H-связи (правило Липински);

## Применение функций к коллекциям

- `[Chem.MolFromSmiles(smi) for smi in smiles_list]` - генерация списка молекул из SMILES;
- `df['mol'] = df['smiles'].apply(Chem.MolFromSmiles)` - создание колонки молекул в DataFrame;
- `df['MW'] = df['mol'].apply(Descriptors.MolWt)` - расчет дескрипторов через apply;

## Работа с реакциями

- `Chem.AllChem.ReactionFromSmarts('[C:1][OH:2]>>[C:1][O:2]C')` - создание реакции из SMARTS;
- `rxn.RunReactants([mol])` - применение реакции к молекуле;
- `Draw.ReactionToImage(rxn)` - визуализация реакции;

## Вывод и экспорт

- `.to_csv()` - сохранение в CSV;  
- `.to_excel()` - сохранение в Excel;  
- `.to_numpy()` - преобразование в numpy массив;