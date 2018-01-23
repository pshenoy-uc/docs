
from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField


class MstState(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(unique=True, max_length=2)
    name = models.CharField(unique=True, max_length=70)

    def __str__(self):
        return '%s' % self.key

    class Meta:
        managed = False
        db_table = 'mst_state'

class UnresolvedStatus(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'unresolved_status'

class AttorneyInfo(models.Model):
    name = models.CharField(max_length=100)
    status = models.ForeignKey('UnresolvedStatus', models.DO_NOTHING)
    mst_state = models.ForeignKey('MstState', models.DO_NOTHING)
    bar_num = models.IntegerField()
    county = models.CharField(max_length=100, blank=True, null=True)
    admitted_date = models.DateField(blank=True, null=True)
    email = ArrayField(models.TextField(blank=True, null=True))
    phone = JSONField(blank=True, null=True)
    law_firm = models.CharField(max_length=500, blank=True, null=True)
    created_date = models.DateField()
    updated_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'attorney_info'
        unique_together = (('mst_state', 'bar_num'),)

class AttorneyFullAddress(models.Model):
    attorney = models.ForeignKey('AttorneyInfo', models.DO_NOTHING)
    complete_address = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attorney_full_address'
        unique_together = (('attorney', 'complete_address'),)

class AttorneyAddress(models.Model):
    attorney = models.ForeignKey('AttorneyInfo', models.DO_NOTHING)
    street_address = models.CharField(max_length=250)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=3, blank=True, null=True)
    country = models.CharField(max_length=30)
    zip = models.CharField(max_length=6, blank=True, null=True)
    zip_4 = models.CharField(max_length=5, blank=True, null=True)
    full_address = models.ForeignKey('AttorneyFullAddress', models.DO_NOTHING, db_column='full_address')

    class Meta:
        managed = False
        db_table = 'attorney_address'
        unique_together = (('attorney', 'street_address'),)

class CustomTableMap(models.Model):
    mst_state = models.ForeignKey('MstState', models.DO_NOTHING)
    table_type = models.CharField(max_length=20)
    custom_table_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'custom_table_map'
        unique_together = (('mst_state', 'table_type'),)

class CustomTexas(models.Model):
    attorney = models.ForeignKey(AttorneyInfo, models.DO_NOTHING, unique=True)
    profile_last_certified = models.DateField(blank=True, null=True)
    practice_area = ArrayField(models.TextField(blank=True, null=True))
    practice_location = ArrayField(models.TextField(blank=True, null=True))
    admittance = JSONField
    firm_size = models.CharField(max_length=50, blank=True, null=True)
    service_provided = JSONField
    occupation = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'custom_texas'

class Downloads(models.Model):
    bar_num = models.IntegerField()
    mst_state = models.ForeignKey('MstState', models.DO_NOTHING)
    html_file_path = models.CharField(max_length=250, unique=True)
    is_parsed = models.BooleanField()
    last_parsed_date = models.DateField(blank=True, null=True)
    created_date = models.DateField()
    last_updated = models.DateField()

    class Meta:
        managed = False
        db_table = 'downloads'
        unique_together = (('bar_num', 'mst_state'),)

class ErrorSeverity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'error_severity'

class ErrorType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'error_type'

class ErrorLog(models.Model):
    stats = models.ForeignKey('StatsExtractor', models.DO_NOTHING)
    attorney = models.ForeignKey(AttorneyInfo, models.DO_NOTHING, blank=True, null=True)
    error_type = models.ForeignKey('ErrorType', models.DO_NOTHING, blank=True, null=True)
    error_severity = models.ForeignKey('ErrorSeverity', models.DO_NOTHING, blank=True, null=True)
    error_msg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'error_log'

class StatsExtractor(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    prefix = models.CharField(max_length=10, blank=True, null=True)
    num_of_bar_num_to_try = models.IntegerField(blank=True, null=True)
    start_bar_num = models.IntegerField(blank=True, null=True)
    end_bar_num = models.BigIntegerField(blank=True, null=True)
    last_successful_bar_num = models.IntegerField(blank=True, null=True)
    success_bar_num_count = models.IntegerField(blank=True, null=True)
    failed_bar_num_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stats_extractor'
