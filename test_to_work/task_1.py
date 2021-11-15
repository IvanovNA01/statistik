import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from pandas._libs.missing import NA

work_dir = Path.cwd()
junior_c_meta_path = work_dir/'test_to_work'/'junior_c_meta.pkl'
junior_d_meta_path = work_dir/'test_to_work'/'junior_d_meta.pkl'
junior_e_open_path = work_dir/'test_to_work'/'junior_e_open.pkl'
junior_e_send_path = work_dir/'test_to_work'/'junior_e_send.pkl'

email_company_data = pd.read_pickle(junior_c_meta_path)
"""ТИПЫ ПИСЕМ с различной информацией о продукции
        ID    BRANDS KEY_MESSAGE CONTENT_TYPE CURRENT_STATUS
  3    165         R        None         None          Draft
  15   182         R        None         None          Draft
  22   557  R, OD, O       Other   Engagement          Draft
  74   416        OD        None         None          Draft
  75   266         R        None         None          Draft
  ..   ...       ...         ...          ...            ...
  918  260         R    Efficacy    Education      Completed
  919  283         R      Safety    Education      Completed
  920  230         R    Efficacy    Education      Completed
  921   94         O     Quality    Education      Completed
  922  248         O    Efficacy    Education      Completed 

  ID.nunique()
  154
  shape
  (154, 5)

  BRANDS.value_counts() бренды косметики
  R           69
  A           26
  OD          25
  O           19
  R, OD, O    15

  KEY_MESSAGE.value_counts() ключевое сообщение имейла
  Other                  54
  Efficacy               29 Эффективность продукта
  Safety                 19 Безопасность 
  Quality                 7 Качество 
  Diagnostic approach     5 метод диагностики
  test                    1

  CONTENT_TYPE.value_counts() тип контента имейла
  Education       70 Образование 
  Engagement      26 Участие 
  Awareness        9 Осведомленность 
  Entertaining     9 Развлекательный

  CURRENT_STATUS.value_counts() статус компании
  Active       71
  Completed    42
  Draft        41 черновой проект
  """
engineer_data = pd.read_pickle(junior_d_meta_path)
""" ИНФА ПО косметологам, которым рассылаем письма
        CITY  REGION1  REGION2  REGION3                            CONTACT_ID  SPECIALTY     SEGMENT 
  0         1     - 1       - 1     - 1  021e1902-2efd-40ce-b3ae-8f43703053f7          0  no segment
  2         1     - 1       - 1     - 1  028edc7a-9e21-46c1-b34b-6bcd5477c33bSEGMENT   0  no segment
  3         1     - 1       - 1     - 1  037c65bb-d5de-4216-a4ed-83b8661dd70c          0  no segment
  4         1     - 1       - 1     - 1  040c709e-bb9f-4402-b9b7-74e3e13ff5f9          0  no segment
  5         1     - 1       - 1     - 1  04984e54-4e62-47c1-bb3b-d8a985413f40          0  no segment
  ...     ...      ...      ...      ...                                   ...        ...         ...
  26861   122       53       84      806  292e2fb0-56d6-4a16-86b0-158fcbb23481          2          D2
  26862   122       53       84      802  19780ba4-8369-4ff1-a4c8-2a93483119bf          2           E
  26863   546       43      189      613  9d733733-d5d9-4b34-a1f4-45c000dca5ec          2           A
  26864   644        5      413       57  8f16656d-6bd9-4661-b5b8-6dedc3c6f3ac          2          D2
  26865   644        5      413       57  2be6b844-192d-42c2-bfdc-16e4447e693c          2           E 
  (25461, 7)

  CITY - город косметолога
  REGION1 - информация о гео-локации
  REGION2 - информация о гео-локации
  REGION3 - информация о гео-локации
  CONTACT_ID - ID инженера
  SPECIALTY - специализация косметолога
  SEGMENT - сегмент косметолога

  CITY.nunique()
  830
  REGION1.nunique()
  85
  engineer_data.CONTACT_ID.nunique()
  25461

  engineer_data.loc[engineer_data.CITY == 1, :].REGION1.nunique() = "-1"
  """
send_mail_data = pd.read_pickle(junior_e_send_path).rename(
    columns={'ACTIVITY_DATE': 'SEND_MAIL_DATE'}).drop('ACTIVITY_TYPE', 1)
"""ПОСЛАННЫЕ ПИСЬМА
                                    CONTACT_ID ASSET_ID ACTIVITY_TYPE            SEND_MAIL_DATE     CAMPAIGN_ID
  0       025cb4d9-c8a2-4337-8d52-9fe86642653f      996     EmailSend  2021-04-05 06:47:43.350  1150.000000000
  1       025cb4d9-c8a2-4337-8d52-9fe86642653f      738     EmailSend  2021-02-25 04:02:15.157   976.000000000
  2       025cb4d9-c8a2-4337-8d52-9fe86642653f      740     EmailSend  2021-02-26 03:00:31.030   979.000000000
  3       45997759-279d-4bda-a1d3-f5561cffa025      906     EmailSend  2021-03-17 11:15:00.133  1053.000000000
  4       45997759-279d-4bda-a1d3-f5561cffa025      737     EmailSend  2021-02-25 04:10:16.123   975.000000000
  ...                                      ...      ...           ...                      ...             ...
  135602  2dd06fe4-522f-442b-8415-7c4d7f5d6d88     1292     EmailSend  2021-05-29 03:30:19.433  1468.000000000
  135603  982f7bfe-9f74-459a-8664-7c0679c044d3     1292     EmailSend  2021-05-29 03:30:20.933  1468.000000000
  135604  a42662bf-e708-4753-97c9-b75a3402b35d     1292     EmailSend  2021-05-29 03:30:22.583  1468.000000000
  135605  6bd687fb-f629-41f1-8aef-97b2e661d054     1292     EmailSend  2021-05-29 03:30:22.583  1468.000000000
  135606  61483a91-4dfa-41b1-8ba9-4d84f264a82e     1292     EmailSend  2021-05-29 03:30:20.933  1468.000000000
  [135607 rows x 5 columns]

  CONTACT_ID - ID косметолога
  ASSET_ID - ID имейла
  ACTIVITY_TYPE - действие над имейлом
  SEND_MAIL_DATE - время совершения действия
  CAMPAIGN_ID - ID email кампании косметолога

  ASSET_ID.nunique()
  278
  CAMPAIGN_ID.nunique()
  182
  send_mail_data.CONTACT_ID.nunique()
  26866

КОЛ-ВО ОТПРАВЛЕННЫХ ПИСЕМ ДЛЯ КАЖДОГО СТИЛИСТА
  reading_mail.groupby('CONTACT_ID', as_index=False).agg({'ASSET_ID': 'count'}).rename(columns={'ASSET_ID': 'COUNT_READING_MAIL'}).sort_values('COUNT_READING_MAIL', ascending=False)
                                  CONTACT_ID  COUNT_READING_MAIL
  2450   1710cc5d-26fe-48c1-9b52-ef2b0163e932                  80
  16328  9b7033dd-67f2-4165-94d1-e23cf700a430                  79
  10112  5ef0a08c-0cd1-4e48-b443-e6cd11978af1                  79
  14390  887d8ec7-b084-4dd1-a987-6a139b448050                  78
  26763  fef7a606-9478-43c5-a877-79be6202702c                  77
  ...                                     ...                 ...
  9595   5a0d6e2c-b0b6-44b6-b2ce-680a8e3768a2                   0
  9594   5a0c8c9d-1cfd-4e5b-b9df-8db459e02569                   0
  9593   5a059caa-2ff5-4d9a-958b-342361840d47                   0
  9591   59fc9684-be45-4161-9194-8efb265de631                   0
  26865  fffd25d0-e4d1-4129-9416-27c4f930a767                   0

  [26866 rows x 2 columns]
  """
open_mail_data = pd.read_pickle(junior_e_open_path).rename(
    columns={'ACTIVITY_DATE': 'READING_MAIL_DATE'})
"""ОТКРЫТЫЕ ПИСЬМА (необходимо максимизировать кол-во прочтенных открытых писем ACTIVITY_TYPE = EmailOpen)
                                    CONTACT_ID ASSET_ID ACTIVITY_TYPE            ACTIVITY_DATE
  0       66d30eed-7a52-4f32-8237-d902beb03eb5     None          None                     None
  1       6dc02d35-5dff-467f-b72a-b4e9f9f81cc5      512     EmailOpen  2020-12-25 21:00:58.340
  2       6dc02d35-5dff-467f-b72a-b4e9f9f81cc5      512     EmailOpen  2020-12-27 01:01:03.287
  3       6dc02d35-5dff-467f-b72a-b4e9f9f81cc5      512     EmailOpen  2020-12-23 13:04:26.560
  4       6dc02d35-5dff-467f-b72a-b4e9f9f81cc5      512     EmailOpen  2020-12-22 09:00:56.913
  ...                                      ...      ...           ...                      ...
  198561  292e2fb0-56d6-4a16-86b0-158fcbb23481     None          None                     None
  198562  19780ba4-8369-4ff1-a4c8-2a93483119bf     None          None                     None
  198563  9d733733-d5d9-4b34-a1f4-45c000dca5ec     None          None                     None
  198564  8f16656d-6bd9-4661-b5b8-6dedc3c6f3ac     None          None                     None
  198565  2be6b844-192d-42c2-bfdc-16e4447e693c     None          None                     None
  [198566 rows x 4 columns]

  CONTACT_ID - ID косметолога
  ASSET_ID - ID имейла
  ACTIVITY_TYPE - действие над имейлом
  ACTIVITY_DATE - время совершения действия

  open_mail_data.CONTACT_ID.nunique()
  26866
  
  open_mail_data.ASSET_ID.nunique()
  247

  open_mail_data.groupby(['ASSET_ID', 'ACTIVITY_TYPE'], as_index=False).count()
      ASSET_ID ACTIVITY_TYPE  CONTACT_ID  ACTIVITY_DATE
  0       1001     EmailOpen         275            275
  1       1004     EmailOpen         695            695
  ..       ...           ...         ...            ...
  246      996     EmailOpen         491            491
  [247 rows x 4 columns]

  open_mail_data.ASSET_ID.isnull().sum() = open_mail_data.ACTIVITY_TYPE.isnull().sum()
  24203
КОЛ-ВО ПОЛУЧЕННЫХ ПИСЕМ ДЛЯ КАЖДОГО СТИЛИСТА
  reading_mail.groupby('CONTACT_ID', as_index=False).agg({'ASSET_ID': 'count'}).rename(columns={'ASSET_ID': 'COUNT_READING_MAIL'}).sort_values('COUNT_READING_MAIL', ascending=False)
                                    CONTACT_ID  COUNT_READING_MAIL
  13541  80ac1a3e-79c1-4484-a4fa-69909569da6a                 448
  7121   4350e95d-0261-42ff-bf4e-04b533d1d861                 412
  3244   1ea0298c-6066-4a3b-af3d-64069a11f488                 409
  12381  75665bf3-8272-44a7-a353-99bb3d86bee8                 378
  24948  ed741fdf-daa6-47e3-9f93-08a7b375c586                 375
  ...                                     ...                 ...
  9368   57eb6e05-fb9d-45a1-8fe2-70919acad488                   1
  9367   57e7f744-8d9f-45cc-900b-12ebc48f614d                   1
  9366   57e7b6e7-8c2c-447c-aa6b-02a6e4990342                   1
  9365   57e559b2-a105-4146-bb92-ebd5a60b8db8                   1
  26865  fffd25d0-e4d1-4129-9416-27c4f930a767                   1
  [26866 rows x 2 columns]
  """

# Замена None на 0
open_mail_data = open_mail_data.fillna(0)
# Прочитанные письма
reading_mail = open_mail_data[open_mail_data.ASSET_ID.astype(int) > 0]
"""ВСЕ ПРОЧИТАННЫЕ
                                    CONTACT_ID ASSET_ID ACTIVITY_TYPE        READING_MAIL_DATE
  1       6dc02d35-5dff-467f-b72a-b4e9f9f81cc5      512     EmailOpen  2020-12-25 21:00:58.340
  2       6dc02d35-5dff-467f-b72a-b4e9f9f81cc5      512     EmailOpen  2020-12-27 01:01:03.287
  3       6dc02d35-5dff-467f-b72a-b4e9f9f81cc5      512     EmailOpen  2020-12-23 13:04:26.560
  4       6dc02d35-5dff-467f-b72a-b4e9f9f81cc5      512     EmailOpen  2020-12-22 09:00:56.913
  5       6dc02d35-5dff-467f-b72a-b4e9f9f81cc5      512     EmailOpen  2020-12-24 17:01:26.817
  ...                                      ...      ...           ...                      ...
  198552  5eceacee-9e50-4dfd-91f1-dc3d9a63a5f9     1095     EmailOpen  2021-05-14 03:30:21.590
  198553  5eceacee-9e50-4dfd-91f1-dc3d9a63a5f9     1095     EmailOpen  2021-05-16 11:30:15.400
  198554  5eceacee-9e50-4dfd-91f1-dc3d9a63a5f9     1201     EmailOpen  2021-05-20 11:34:39.173
  198555  5eceacee-9e50-4dfd-91f1-dc3d9a63a5f9     1153     EmailOpen  2021-05-14 03:14:59.357
  198556  5eceacee-9e50-4dfd-91f1-dc3d9a63a5f9     1153     EmailOpen  2021-05-16 11:14:52.603

  [174363 rows x 4 columns]

КОЛИЧЕСТВО ПРОЧИТАННЫХ ДЛЯ КАЖДОГО СТИЛИСТА
  reading_mail.groupby('CONTACT_ID', as_index=False).agg({'ASSET_ID': 'count'}).rename(columns={'ASSET_ID': 'COUNT_READING_MAIL'}).sort_values('COUNT_READING_MAIL', ascending=False)
                                  CONTACT_ID  COUNT_READING_MAIL
  1361  80ac1a3e-79c1-4484-a4fa-69909569da6a                 448
  699   4350e95d-0261-42ff-bf4e-04b533d1d861                 412
  312   1ea0298c-6066-4a3b-af3d-64069a11f488                 409
  1245  75665bf3-8272-44a7-a353-99bb3d86bee8                 378
  2470  ed741fdf-daa6-47e3-9f93-08a7b375c586                 375
  ...                                    ...                 ...
  2161  cf0a682d-b7eb-483a-8829-bf05775bd593                   1
  2150  ce7d43a4-c9e5-4767-ba53-69ce99d1c339                   1
  2144  ce29ae5c-cf4a-4cbd-b27f-4282e0cbe57d                   1
  2510  f13f0e66-2c3c-4403-9998-88795141c0b9                   1
  944   5b8846c1-4927-49b1-868b-87e7b4a87c1c                   1
  [2663 rows x 2 columns]
  """
mindate_send_mail = send_mail_data

print(send_mail_data.SEND_MAIL_DATE.min())
