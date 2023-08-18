# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bom(models.Model):
    uid = models.AutoField(primary_key=True)
    no = models.CharField(max_length=11, blank=True, null=True)
    partnumber = models.CharField(db_column='partNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=400, blank=True, null=True)  # Field name made lowercase.
    sellingprice = models.CharField(db_column='sellingPrice', max_length=11, blank=True, null=True)  # Field name made lowercase.
    purchaseprice = models.CharField(db_column='purchasePrice', max_length=11, blank=True, null=True)  # Field name made lowercase.
    productionlocation = models.CharField(db_column='productionLocation', max_length=30, blank=True, null=True)  # Field name made lowercase.
    packing_note = models.CharField(db_column='Packing_Note', max_length=30, blank=True, null=True)  # Field name made lowercase.
    quantity_pack = models.CharField(db_column='quantity_PACK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    quantity_box = models.CharField(db_column='quantity_BOX', max_length=11, blank=True, null=True)  # Field name made lowercase.
    packing2_note = models.CharField(db_column='Packing2_Note', max_length=30, blank=True, null=True)  # Field name made lowercase.
    quantity_pack2 = models.CharField(db_column='quantity_PACK2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    quantity_box2 = models.CharField(db_column='quantity_BOX2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    trayname1 = models.CharField(db_column='trayName1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    requirement1 = models.CharField(max_length=11, blank=True, null=True)
    covername2 = models.CharField(db_column='coverName2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    requirement2 = models.CharField(max_length=11, blank=True, null=True)
    covername3 = models.CharField(db_column='coverName3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    requirement3 = models.CharField(max_length=11, blank=True, null=True)
    covername4 = models.CharField(db_column='coverName4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    requirement4 = models.CharField(max_length=11, blank=True, null=True)
    remaininglocation = models.CharField(max_length=30, blank=True, null=True)
    part1 = models.CharField(max_length=30, blank=True, null=True)
    hs_gcavity = models.CharField(db_column='HS_GCavity', max_length=30, blank=True, null=True)  # Field name made lowercase.
    productname1 = models.CharField(db_column='productName1', max_length=400, blank=True, null=True)  # Field name made lowercase.
    usage1 = models.CharField(db_column='USAGE1', max_length=11, blank=True, null=True)  # Field name made lowercase.
    part2 = models.CharField(max_length=30, blank=True, null=True)
    productname2 = models.CharField(db_column='productName2', max_length=400, blank=True, null=True)  # Field name made lowercase.
    usage2 = models.CharField(db_column='USAGE2', max_length=11, blank=True, null=True)  # Field name made lowercase.
    part3 = models.CharField(max_length=30, blank=True, null=True)
    productname3 = models.CharField(db_column='productName3', max_length=400, blank=True, null=True)  # Field name made lowercase.
    usage3 = models.CharField(db_column='USAGE3', max_length=11, blank=True, null=True)  # Field name made lowercase.
    part4 = models.CharField(max_length=30, blank=True, null=True)
    productname4 = models.CharField(db_column='productName4', max_length=400, blank=True, null=True)  # Field name made lowercase.
    usage4 = models.CharField(db_column='USAGE4', max_length=11, blank=True, null=True)  # Field name made lowercase.
    part5 = models.CharField(max_length=30, blank=True, null=True)
    productname5 = models.CharField(db_column='productName5', max_length=400, blank=True, null=True)  # Field name made lowercase.
    usage5 = models.CharField(db_column='USAGE5', max_length=11, blank=True, null=True)  # Field name made lowercase.
    part6 = models.CharField(max_length=30, blank=True, null=True)
    productname6 = models.CharField(db_column='productName6', max_length=400, blank=True, null=True)  # Field name made lowercase.
    usage6 = models.CharField(db_column='USAGE6', max_length=11, blank=True, null=True)  # Field name made lowercase.
    inspectiondimensionrange1 = models.CharField(db_column='InspectionDimensionRange1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    inspectiondimensionrange2 = models.CharField(db_column='InspectionDimensionRange2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    inspectiondimensionrange3 = models.CharField(db_column='InspectionDimensionRange3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    inspectiondimensionrange4 = models.CharField(db_column='InspectionDimensionRange4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    inspectiondimensionrange5 = models.CharField(db_column='InspectionDimensionRange5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    inspectiondimensiondrawing = models.CharField(db_column='InspectionDimensionDrawing', max_length=30, blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOM'


class BomBackup(models.Model):
    uid = models.AutoField(primary_key=True)
    no = models.CharField(max_length=11, blank=True, null=True)
    partnumber = models.CharField(db_column='partNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=400, blank=True, null=True)  # Field name made lowercase.
    sellingprice = models.CharField(db_column='sellingPrice', max_length=11, blank=True, null=True)  # Field name made lowercase.
    purchaseprice = models.CharField(db_column='purchasePrice', max_length=11, blank=True, null=True)  # Field name made lowercase.
    productionlocation = models.CharField(db_column='productionLocation', max_length=30, blank=True, null=True)  # Field name made lowercase.
    packing_note = models.CharField(db_column='Packing_Note', max_length=30, blank=True, null=True)  # Field name made lowercase.
    quantity_pack = models.CharField(db_column='quantity_PACK', max_length=11, blank=True, null=True)  # Field name made lowercase.
    quantity_box = models.CharField(db_column='quantity_BOX', max_length=11, blank=True, null=True)  # Field name made lowercase.
    packing2_note = models.CharField(db_column='Packing2_Note', max_length=30, blank=True, null=True)  # Field name made lowercase.
    quantity_pack2 = models.CharField(db_column='quantity_PACK2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    quantity_box2 = models.CharField(db_column='quantity_BOX2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    trayname1 = models.CharField(db_column='trayName1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    requirement1 = models.CharField(max_length=11, blank=True, null=True)
    covername2 = models.CharField(db_column='coverName2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    requirement2 = models.CharField(max_length=11, blank=True, null=True)
    covername3 = models.CharField(db_column='coverName3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    requirement3 = models.CharField(max_length=11, blank=True, null=True)
    covername4 = models.CharField(db_column='coverName4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    requirement4 = models.CharField(max_length=11, blank=True, null=True)
    remaininglocation = models.CharField(max_length=30, blank=True, null=True)
    part1 = models.CharField(max_length=30, blank=True, null=True)
    hs_gcavity = models.CharField(db_column='HS_GCavity', max_length=30, blank=True, null=True)  # Field name made lowercase.
    productname1 = models.CharField(db_column='productName1', max_length=400, blank=True, null=True)  # Field name made lowercase.
    usage1 = models.CharField(db_column='USAGE1', max_length=11, blank=True, null=True)  # Field name made lowercase.
    part2 = models.CharField(max_length=30, blank=True, null=True)
    productname2 = models.CharField(db_column='productName2', max_length=400, blank=True, null=True)  # Field name made lowercase.
    usage2 = models.CharField(db_column='USAGE2', max_length=11, blank=True, null=True)  # Field name made lowercase.
    part3 = models.CharField(max_length=30, blank=True, null=True)
    productname3 = models.CharField(db_column='productName3', max_length=400, blank=True, null=True)  # Field name made lowercase.
    usage3 = models.CharField(db_column='USAGE3', max_length=11, blank=True, null=True)  # Field name made lowercase.
    part4 = models.CharField(max_length=30, blank=True, null=True)
    productname4 = models.CharField(db_column='productName4', max_length=400, blank=True, null=True)  # Field name made lowercase.
    usage4 = models.CharField(db_column='USAGE4', max_length=11, blank=True, null=True)  # Field name made lowercase.
    part5 = models.CharField(max_length=30, blank=True, null=True)
    productname5 = models.CharField(db_column='productName5', max_length=400, blank=True, null=True)  # Field name made lowercase.
    usage5 = models.CharField(db_column='USAGE5', max_length=11, blank=True, null=True)  # Field name made lowercase.
    part6 = models.CharField(max_length=30, blank=True, null=True)
    productname6 = models.CharField(db_column='productName6', max_length=400, blank=True, null=True)  # Field name made lowercase.
    usage6 = models.CharField(db_column='USAGE6', max_length=11, blank=True, null=True)  # Field name made lowercase.
    inspectiondimensionrange1 = models.CharField(db_column='InspectionDimensionRange1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    inspectiondimensionrange2 = models.CharField(db_column='InspectionDimensionRange2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    inspectiondimensionrange3 = models.CharField(db_column='InspectionDimensionRange3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    inspectiondimensionrange4 = models.CharField(db_column='InspectionDimensionRange4', max_length=30, blank=True, null=True)  # Field name made lowercase.
    inspectiondimensionrange5 = models.CharField(db_column='InspectionDimensionRange5', max_length=30, blank=True, null=True)  # Field name made lowercase.
    inspectiondimensiondrawing = models.CharField(db_column='InspectionDimensionDrawing', max_length=30, blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOM_Backup'


class DefectLog(models.Model):
    uid = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    partno = models.CharField(db_column='PartNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lotno = models.CharField(db_column='lotNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    quantity = models.CharField(max_length=10, blank=True, null=True)
    quantity2 = models.CharField(max_length=10, blank=True, null=True)
    quantity3 = models.IntegerField()
    worker = models.CharField(db_column='Worker', max_length=100, blank=True, null=True)  # Field name made lowercase.
    defect_note = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Defect_log'


class Worker(models.Model):
    wid = models.AutoField(primary_key=True)
    workername = models.CharField(db_column='workerName', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Worker'


class Assembly(models.Model):
    uid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=30)
    partnumber = models.CharField(db_column='partNumber', max_length=30)  # Field name made lowercase.
    quantity = models.IntegerField()
    lotno = models.CharField(db_column='lotNo', max_length=30)  # Field name made lowercase.
    assemblydate = models.DateTimeField(db_column='assemblyDate')  # Field name made lowercase.
    assemblyworker = models.CharField(db_column='assemblyWorker', max_length=100)  # Field name made lowercase.
    assemblypn = models.CharField(db_column='assemblyPN', max_length=30)  # Field name made lowercase.
    assemblyquantity = models.IntegerField(db_column='assemblyQuantity')  # Field name made lowercase.
    remainingquantity = models.IntegerField(db_column='remainingQuantity')  # Field name made lowercase.
    note = models.CharField(max_length=100)
    assembly_no = models.CharField(db_column='Assembly_No', max_length=20)  # Field name made lowercase.
    assembly_usage = models.IntegerField(db_column='Assembly_USAGE', blank=True, null=True)  # Field name made lowercase.
    usage1 = models.IntegerField(db_column='USAGE1', blank=True, null=True)  # Field name made lowercase.
    makeinspectionnum = models.CharField(db_column='makeInspectionNum', max_length=5)  # Field name made lowercase.
    warehouse = models.CharField(max_length=15, blank=True, null=True)
    assemblydate2 = models.DateTimeField(db_column='assemblyDate2')  # Field name made lowercase.
    visible = models.IntegerField()
    assemblyquantity2 = models.CharField(db_column='assemblyQuantity2', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assembly'


class Assembly2(models.Model):
    uid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=30)
    partnumber = models.CharField(db_column='partNumber', max_length=30)  # Field name made lowercase.
    quantity = models.CharField(max_length=11)
    lotno = models.CharField(db_column='lotNo', max_length=30)  # Field name made lowercase.
    assemblydate = models.DateTimeField(db_column='assemblyDate')  # Field name made lowercase.
    assemblyworker = models.CharField(db_column='assemblyWorker', max_length=100)  # Field name made lowercase.
    assemblypn = models.CharField(db_column='assemblyPN', max_length=30)  # Field name made lowercase.
    assemblyquantity = models.CharField(db_column='assemblyQuantity', max_length=11)  # Field name made lowercase.
    remainingquantity = models.CharField(db_column='remainingQuantity', max_length=11)  # Field name made lowercase.
    note = models.CharField(max_length=100)
    assembly_no = models.CharField(db_column='Assembly_No', max_length=20)  # Field name made lowercase.
    assembly_usage = models.CharField(db_column='Assembly_USAGE', max_length=11, blank=True, null=True)  # Field name made lowercase.
    usage1 = models.CharField(db_column='USAGE1', max_length=11, blank=True, null=True)  # Field name made lowercase.
    checkinspection = models.CharField(db_column='checkInspection', max_length=5)  # Field name made lowercase.
    warehouse = models.CharField(max_length=15, blank=True, null=True)
    defect = models.CharField(max_length=50, blank=True, null=True)
    visible = models.IntegerField()
    assemblyquantity2 = models.CharField(db_column='assemblyQuantity2', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assembly2'


class AssemblyHalf(models.Model):
    uid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=30)
    partnumber = models.CharField(db_column='partNumber', max_length=30)  # Field name made lowercase.
    quantity = models.IntegerField()
    lotno = models.CharField(db_column='lotNo', max_length=30)  # Field name made lowercase.
    assemblydate = models.DateTimeField(db_column='assemblyDate')  # Field name made lowercase.
    assemblyworker = models.CharField(db_column='assemblyWorker', max_length=100)  # Field name made lowercase.
    assemblypn = models.CharField(db_column='assemblyPN', max_length=30)  # Field name made lowercase.
    assemblyquantity = models.IntegerField(db_column='assemblyQuantity')  # Field name made lowercase.
    remainingquantity = models.IntegerField(db_column='remainingQuantity')  # Field name made lowercase.
    note = models.CharField(max_length=100)
    assembly_no = models.CharField(db_column='Assembly_No', max_length=20)  # Field name made lowercase.
    assembly_usage = models.IntegerField(db_column='Assembly_USAGE', blank=True, null=True)  # Field name made lowercase.
    usage1 = models.IntegerField(db_column='USAGE1', blank=True, null=True)  # Field name made lowercase.
    makeinspectionnum = models.CharField(db_column='makeInspectionNum', max_length=5)  # Field name made lowercase.
    warehouse = models.CharField(max_length=15, blank=True, null=True)
    assemblydate2 = models.DateTimeField(db_column='assemblyDate2')  # Field name made lowercase.
    visible = models.IntegerField()
    assemblyquantity2 = models.CharField(db_column='assemblyQuantity2', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assembly_half'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Currentremainassemblycomplete(models.Model):
    assemblypn = models.CharField(db_column='assemblyPN', max_length=30)  # Field name made lowercase.
    remainquantity = models.IntegerField(db_column='remainQuantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currentRemainAssemblyComplete'


class DataLog(models.Model):
    uid = models.AutoField(primary_key=True)
    datetime = models.DateField(db_column='DateTime')  # Field name made lowercase.
    all_count = models.IntegerField(db_column='All_count', blank=True, null=True)  # Field name made lowercase.
    today_count = models.IntegerField(db_column='Today_count', blank=True, null=True)  # Field name made lowercase.
    defect_count = models.IntegerField(db_column='Defect_count', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_log'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ExternalImportinspection(models.Model):
    uid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=30)
    partnumber = models.CharField(db_column='partNumber', max_length=30)  # Field name made lowercase.
    quantity = models.IntegerField()
    lotno = models.CharField(db_column='lotNo', max_length=30)  # Field name made lowercase.
    importinspectiondate = models.DateField(db_column='importInspectionDate')  # Field name made lowercase.
    importinspectionworker = models.CharField(db_column='importInspectionWorker', max_length=30)  # Field name made lowercase.
    defect = models.CharField(max_length=30)
    note = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'external_importInspection'


class ExternalWarehousing(models.Model):
    uid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=30)
    partnumber = models.CharField(db_column='partNumber', max_length=30)  # Field name made lowercase.
    quantity = models.IntegerField()
    lotno = models.CharField(db_column='lotNo', max_length=30)  # Field name made lowercase.
    warehousingdate = models.DateField(db_column='warehousingDate')  # Field name made lowercase.
    warehousingworker = models.CharField(db_column='warehousingWorker', max_length=30)  # Field name made lowercase.
    note = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'external_warehousing'


class Importinspection(models.Model):
    uid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=30)
    partnumber = models.CharField(db_column='partNumber', max_length=30)  # Field name made lowercase.
    quantity = models.IntegerField()
    quantity2 = models.CharField(max_length=10, blank=True, null=True)
    lotno = models.CharField(db_column='lotNo', max_length=30)  # Field name made lowercase.
    importinspectiondate = models.DateTimeField(db_column='importInspectionDate')  # Field name made lowercase.
    importinspectionworker = models.CharField(db_column='importInspectionWorker', max_length=100)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    defect = models.CharField(max_length=30, blank=True, null=True)
    visual = models.IntegerField(blank=True, null=True)
    foreignmaterial = models.IntegerField(db_column='foreignMaterial', blank=True, null=True)  # Field name made lowercase.
    labelerror = models.IntegerField(db_column='labelError', blank=True, null=True)  # Field name made lowercase.
    incorrect = models.IntegerField(blank=True, null=True)
    improveditem = models.CharField(db_column='improvedItem', max_length=30, blank=True, null=True)  # Field name made lowercase.
    etc = models.CharField(max_length=30)
    note = models.CharField(max_length=100, blank=True, null=True)
    barcode = models.CharField(max_length=30, blank=True, null=True)
    use_location = models.CharField(db_column='Use_Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    visible = models.IntegerField()
    cancel_note = models.CharField(db_column='Cancel_note', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bad_shape = models.IntegerField(db_column='Bad shape')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_before_improvement = models.IntegerField(db_column='Part before improvement')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'importInspection'


class Log(models.Model):
    uid = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    partno = models.CharField(db_column='PartNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lotno = models.CharField(db_column='lotNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    quantity = models.CharField(max_length=10, blank=True, null=True)
    quantity2 = models.CharField(max_length=10, blank=True, null=True)
    worker = models.CharField(db_column='Worker', max_length=100, blank=True, null=True)  # Field name made lowercase.
    before_location = models.CharField(db_column='before_Location', max_length=10, blank=True, null=True)  # Field name made lowercase.
    after_location = models.CharField(db_column='after_Location', max_length=10, blank=True, null=True)  # Field name made lowercase.
    before_state = models.CharField(db_column='before_State', max_length=10, blank=True, null=True)  # Field name made lowercase.
    after_state = models.CharField(db_column='after_State', max_length=10, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(max_length=20, blank=True, null=True)
    bf_table = models.CharField(max_length=50)
    af_table = models.CharField(max_length=50)
    assembly_no = models.CharField(db_column='Assembly_No', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log'


class Member(models.Model):
    uid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    username = models.CharField(db_column='UserName', max_length=30)  # Field name made lowercase.
    wearing = models.CharField(db_column='Wearing', max_length=5)  # Field name made lowercase.
    importinspection = models.CharField(db_column='ImportInspection', max_length=5)  # Field name made lowercase.
    storeroom = models.CharField(db_column='StoreRoom', max_length=5)  # Field name made lowercase.
    assembly = models.CharField(db_column='Assembly', max_length=5)  # Field name made lowercase.
    visualinspection = models.CharField(db_column='VisualInspection', max_length=5)  # Field name made lowercase.
    packaging = models.CharField(db_column='Packaging', max_length=5)  # Field name made lowercase.
    shipmentinspection = models.CharField(db_column='ShipmentInspection', max_length=5)  # Field name made lowercase.
    shipment = models.CharField(db_column='Shipment', max_length=5)  # Field name made lowercase.
    onlybarcode = models.CharField(db_column='OnlyBarcode', max_length=5)  # Field name made lowercase.
    checkbox = models.CharField(db_column='CheckBox', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member'


class Packaging(models.Model):
    uid = models.AutoField(primary_key=True)
    inspectionnum = models.CharField(db_column='inspectionNum', max_length=30)  # Field name made lowercase.
    state = models.CharField(max_length=30)
    assemblypn = models.CharField(db_column='assemblyPN', max_length=30)  # Field name made lowercase.
    partnumber = models.CharField(db_column='partNumber', max_length=30)  # Field name made lowercase.
    quantity = models.IntegerField()
    lotno = models.CharField(db_column='lotNo', max_length=30)  # Field name made lowercase.
    normalcount = models.IntegerField(db_column='normalCount')  # Field name made lowercase.
    boxcount = models.IntegerField(db_column='boxCount')  # Field name made lowercase.
    packagingcommitdate = models.DateTimeField(db_column='packagingCommitDate')  # Field name made lowercase.
    packagingcommitworker = models.CharField(db_column='packagingCommitWorker', max_length=30)  # Field name made lowercase.
    note = models.CharField(max_length=100)
    packingcount = models.IntegerField(db_column='packingCount')  # Field name made lowercase.
    checkpackaging = models.CharField(db_column='checkPackaging', max_length=5)  # Field name made lowercase.
    visualinspectionworker = models.CharField(db_column='visualInspectionWorker', max_length=50)  # Field name made lowercase.
    visualinspectioncount = models.IntegerField(db_column='visualInspectionCount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'packaging'


class Processstate(models.Model):
    uid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=30)
    partnumber = models.DateField(db_column='partNumber')  # Field name made lowercase.
    quantity = models.DateField()
    lotno = models.DateField(db_column='lotNo')  # Field name made lowercase.
    receivingdate = models.DateField(db_column='receivingDate')  # Field name made lowercase.
    importinspectiondatewaiting = models.DateField(db_column='importInspectionDateWaiting')  # Field name made lowercase.
    importinspectiondatecomplete = models.DateField(db_column='importInspectionDateComplete')  # Field name made lowercase.
    warehousingdatewaiting = models.DateField(db_column='warehousingDateWaiting')  # Field name made lowercase.
    warehousingdatecomplete = models.DateField(db_column='warehousingDateComplete')  # Field name made lowercase.
    assemblydatewaiting = models.DateField(db_column='assemblyDateWaiting')  # Field name made lowercase.
    assemblydatecomplete = models.DateField(db_column='assemblyDateComplete')  # Field name made lowercase.
    visualinspectiondatewaiting = models.DateField(db_column='visualInspectionDateWaiting')  # Field name made lowercase.
    visualinspectiondatecomplete = models.DateField(db_column='visualInspectionDateComplete')  # Field name made lowercase.
    packagingdatewaiting = models.DateField(db_column='packagingDateWaiting')  # Field name made lowercase.
    packagingdatecomplete = models.DateField(db_column='packagingDateComplete')  # Field name made lowercase.
    releasedatewaiting = models.DateField(db_column='releaseDateWaiting')  # Field name made lowercase.
    releasedatecomplete = models.DateField(db_column='releaseDateComplete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'processState'


class Receiving(models.Model):
    uid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=30)
    partnumber = models.CharField(db_column='partNumber', max_length=30)  # Field name made lowercase.
    quantity = models.IntegerField()
    lotno = models.CharField(db_column='lotNo', max_length=30)  # Field name made lowercase.
    receivingdate = models.DateTimeField(db_column='receivingDate')  # Field name made lowercase.
    receivingworker = models.CharField(db_column='receivingWorker', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'receiving'


class Release(models.Model):
    uid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=30)
    partnumber = models.CharField(db_column='partNumber', max_length=30)  # Field name made lowercase.
    quantity = models.IntegerField()
    lotno = models.CharField(db_column='lotNo', max_length=30)  # Field name made lowercase.
    releaseworker = models.CharField(db_column='releaseWorker', max_length=30, blank=True, null=True)  # Field name made lowercase.
    releaselocation = models.CharField(db_column='releaseLocation', max_length=30, blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    note = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'release'


class Remainassemblycomplete(models.Model):
    uid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=30)
    partnumber = models.CharField(db_column='partNumber', max_length=30)  # Field name made lowercase.
    quantity = models.IntegerField()
    lotno = models.CharField(db_column='lotNo', max_length=30)  # Field name made lowercase.
    packagingcommitdate = models.DateTimeField(db_column='packagingCommitDate')  # Field name made lowercase.
    packagingcommitworker = models.CharField(db_column='packagingCommitWorker', max_length=30)  # Field name made lowercase.
    assemblypn = models.CharField(db_column='assemblyPN', max_length=30)  # Field name made lowercase.
    remainquantity = models.IntegerField(db_column='remainQuantity')  # Field name made lowercase.
    remainlotno = models.CharField(db_column='remainLotNo', max_length=30)  # Field name made lowercase.
    note = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'remainAssemblyComplete'


class Setinspectionnum(models.Model):
    uid = models.AutoField(primary_key=True)
    inspectionnum = models.CharField(db_column='inspectionNum', max_length=30)  # Field name made lowercase.
    state = models.CharField(max_length=30)
    worknum = models.CharField(db_column='workNum', max_length=30)  # Field name made lowercase.
    partnumber = models.CharField(db_column='partNumber', max_length=30)  # Field name made lowercase.
    quantity = models.IntegerField()
    lotno = models.CharField(db_column='lotNo', max_length=30)  # Field name made lowercase.
    inspectionnumsetdate = models.DateTimeField(db_column='inspectionNumSetDate')  # Field name made lowercase.
    inspectionnumsetworker = models.CharField(db_column='inspectionNumSetWorker', max_length=30)  # Field name made lowercase.
    assemblypn = models.CharField(db_column='assemblyPN', max_length=30)  # Field name made lowercase.
    assemblyquantity = models.IntegerField(db_column='assemblyQuantity')  # Field name made lowercase.
    note = models.CharField(max_length=100)
    checkinspection = models.CharField(db_column='checkInspection', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'setInspectionNum'


class Shipment(models.Model):
    uid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=30)
    assemblypn = models.CharField(db_column='assemblyPN', max_length=30)  # Field name made lowercase.
    shippinginspectiondate = models.DateTimeField(db_column='shippingInspectionDate')  # Field name made lowercase.
    shippinginspectionworker = models.CharField(db_column='shippingInspectionWorker', max_length=30)  # Field name made lowercase.
    boxcount = models.IntegerField(db_column='boxCount')  # Field name made lowercase.
    normalcount = models.IntegerField(db_column='normalCount')  # Field name made lowercase.
    barcodenum = models.CharField(db_column='barcodeNum', max_length=30)  # Field name made lowercase.
    note = models.CharField(max_length=100)
    checkshipment = models.CharField(db_column='checkShipment', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shipment'


class Shipmentcomplete(models.Model):
    uid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=30)
    assemblypn = models.CharField(db_column='assemblyPN', max_length=30)  # Field name made lowercase.
    shippingdate = models.DateTimeField(db_column='shippingDate')  # Field name made lowercase.
    shippingworker = models.CharField(db_column='shippingWorker', max_length=30)  # Field name made lowercase.
    boxcount = models.IntegerField(db_column='boxCount')  # Field name made lowercase.
    normalcount = models.IntegerField(db_column='normalCount')  # Field name made lowercase.
    barcodenum = models.CharField(db_column='barcodeNum', max_length=30)  # Field name made lowercase.
    note = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'shipmentComplete'


class Shipmentinspection(models.Model):
    uid = models.AutoField(primary_key=True)
    inspectionnum = models.CharField(db_column='inspectionNum', max_length=30)  # Field name made lowercase.
    state = models.CharField(max_length=30)
    assemblypn = models.CharField(db_column='assemblyPN', max_length=30)  # Field name made lowercase.
    partnumber = models.CharField(db_column='partNumber', max_length=30)  # Field name made lowercase.
    normalcount = models.IntegerField(db_column='normalCount')  # Field name made lowercase.
    boxcount = models.IntegerField(db_column='boxCount')  # Field name made lowercase.
    packagingdate = models.DateTimeField(db_column='packagingDate')  # Field name made lowercase.
    packagingworker = models.CharField(db_column='packagingWorker', max_length=30)  # Field name made lowercase.
    note = models.CharField(max_length=100)
    barcodenum = models.CharField(db_column='barcodeNum', max_length=30)  # Field name made lowercase.
    checkinspection = models.CharField(db_column='checkInspection', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shipmentInspection'


class Stockwarehouse(models.Model):
    uid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=30)
    partnumber = models.CharField(db_column='partNumber', max_length=30)  # Field name made lowercase.
    quantity = models.IntegerField()
    lotno = models.CharField(db_column='lotNo', max_length=30)  # Field name made lowercase.
    stockwarehousedate = models.DateTimeField(db_column='stockWarehouseDate')  # Field name made lowercase.
    stockwarehouseworker = models.CharField(db_column='stockWarehouseWorker', max_length=30)  # Field name made lowercase.
    warehouselocation = models.CharField(db_column='warehouseLocation', max_length=30, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stockWarehouse'


class UserTable(models.Model):
    uid = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    user_password = models.TextField()
    team = models.CharField(max_length=100)
    registered = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'user_table'


class Visualinsepctionchecklist(models.Model):
    fid = models.AutoField(primary_key=True)
    partnm = models.CharField(db_column='partNM', max_length=30)  # Field name made lowercase.
    faulttype = models.CharField(db_column='faultType', max_length=15)  # Field name made lowercase.
    housing_cover_mainbody = models.IntegerField()
    spacer_cpa = models.IntegerField()
    lever = models.IntegerField()
    holder = models.IntegerField()
    retainer = models.IntegerField()
    innerseal = models.IntegerField(db_column='innerSeal')  # Field name made lowercase.
    gasket = models.IntegerField()
    blockseal = models.IntegerField(db_column='blockSeal')  # Field name made lowercase.
    cap = models.IntegerField()
    us = models.IntegerField()
    positive = models.IntegerField()
    license = models.IntegerField()
    spring = models.IntegerField()
    slide = models.IntegerField()
    note = models.CharField(max_length=30)
    assemblypn = models.CharField(db_column='assemblyPN', max_length=30)  # Field name made lowercase.
    inspectionnum = models.CharField(db_column='inspectionNum', max_length=30)  # Field name made lowercase.
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'visualInsepctionCheckList'


class Visualinspection(models.Model):
    uid = models.AutoField(primary_key=True)
    inspectionnum = models.CharField(db_column='inspectionNum', max_length=30)  # Field name made lowercase.
    state = models.CharField(max_length=30)
    assemblypn = models.CharField(db_column='assemblyPN', max_length=30)  # Field name made lowercase.
    partnumber = models.CharField(db_column='partNumber', max_length=30)  # Field name made lowercase.
    quantity = models.IntegerField()
    lotno = models.CharField(db_column='lotNo', max_length=30)  # Field name made lowercase.
    assemblyquantity = models.IntegerField(db_column='assemblyQuantity')  # Field name made lowercase.
    normalcount = models.IntegerField(db_column='normalCount')  # Field name made lowercase.
    faultycount = models.IntegerField(db_column='faultyCount')  # Field name made lowercase.
    faultypercent = models.FloatField(db_column='faultyPercent')  # Field name made lowercase.
    visualinspectiondate = models.DateTimeField(db_column='visualInspectionDate')  # Field name made lowercase.
    visualinspectionworker = models.CharField(db_column='visualInspectionWorker', max_length=255)  # Field name made lowercase.
    note = models.CharField(max_length=100)
    checkpackaging = models.CharField(db_column='checkPackaging', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'visualInspection'


class WarehouseManager(models.Model):
    uid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    warehouse = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_Manager'


class Warehousing(models.Model):
    uid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=30)
    partnumber = models.CharField(db_column='partNumber', max_length=30)  # Field name made lowercase.
    quantity = models.IntegerField()
    lotno = models.CharField(db_column='lotNo', max_length=30)  # Field name made lowercase.
    warehousingdate = models.DateTimeField(db_column='warehousingDate')  # Field name made lowercase.
    warehousingworker = models.CharField(db_column='warehousingWorker', max_length=30)  # Field name made lowercase.
    improveditem = models.CharField(db_column='improvedItem', max_length=20)  # Field name made lowercase.
    note = models.CharField(max_length=100)
    laststate = models.CharField(db_column='lastState', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'warehousing'


class Work(models.Model):
    state = models.CharField(max_length=100)
    connect = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'work'
