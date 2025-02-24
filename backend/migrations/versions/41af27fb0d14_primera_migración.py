"""Primera migración

Revision ID: 41af27fb0d14
Revises: 
Create Date: 2025-02-10 00:51:39.007583

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '41af27fb0d14'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('email')

    op.drop_table('users')
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.drop_index('email')
        batch_op.drop_index('id_user')

    op.drop_table('employees')
    op.drop_table('payments')
    op.drop_table('spare_parts_inventory')
    op.drop_table('advertisements')
    op.drop_table('session_tokens')
    op.drop_table('appoiments')
    with op.batch_alter_table('clients', schema=None) as batch_op:
        batch_op.drop_index('email')

    op.drop_table('clients')
    op.drop_table('repair_details')
    op.drop_table('vehicles')
    op.drop_table('invoices')
    op.drop_table('messages')
    op.drop_table('chat_messages')
    op.drop_table('repair_orders')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('repair_orders',
    sa.Column('id_order', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('id_client', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('start_date', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=False),
    sa.Column('end_date', mysql.DATETIME(), nullable=True),
    sa.Column('status', mysql.ENUM('Pendiente', 'En proceso', 'Completado', 'Cancelado'), server_default=sa.text("'Pendiente'"), nullable=False),
    sa.Column('total', mysql.DECIMAL(precision=10, scale=2), server_default=sa.text('0.00'), nullable=False),
    sa.Column('id_vehicle', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('entry_date', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=False),
    sa.Column('estimated_delivery_date', mysql.DATETIME(), nullable=False),
    sa.Column('state', mysql.ENUM('Pendiente', 'En proceso', 'Completado', 'cancelado'), nullable=False),
    sa.Column('estimated_total', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('finish_total', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['id_client'], ['clients.id_client'], name='fk_repair_order_clients'),
    sa.ForeignKeyConstraint(['id_client'], ['users.id_user'], name='fk_repair_orders_client', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_vehicle'], ['vehicles.id_vehicle'], name='fk_repair_order_vehicles'),
    sa.ForeignKeyConstraint(['id_vehicle'], ['vehicles.id_vehicle'], name='fk_repair_orders_vehicle', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_order'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('chat_messages',
    sa.Column('id_message', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('id_client', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('id_employee', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('message_text', mysql.TEXT(), nullable=False),
    sa.Column('shipping_date', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=False),
    sa.Column('ready', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_client'], ['users.id_user'], name='fk_chat_message_id_client'),
    sa.ForeignKeyConstraint(['id_employee'], ['users.id_user'], name='fk_chat_message_id_employee'),
    sa.PrimaryKeyConstraint('id_message'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('messages',
    sa.Column('id_message', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('id_user', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('phone', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('message_text', mysql.TEXT(), nullable=False),
    sa.Column('shipping_date', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=False),
    sa.Column('state', mysql.ENUM('Pendiente', 'En gestión', 'Respondido'), nullable=False),
    sa.Column('response_text', mysql.TEXT(), nullable=True),
    sa.Column('response_date', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['users.id_user'], name='fk_messages_user', onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id_message'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('invoices',
    sa.Column('id_invoice', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('id_order', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('id_client', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('issue_date', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=False),
    sa.Column('total', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['id_client'], ['clients.id_client'], name='fk_invoices_client'),
    sa.ForeignKeyConstraint(['id_order'], ['repair_orders.id_order'], name='fk_invoices_order'),
    sa.ForeignKeyConstraint(['id_order'], ['repair_orders.id_order'], name='fk_invoices_repair_order', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_invoice'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('vehicles',
    sa.Column('id_vehicle', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('id_client', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('brand', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('model', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('year', mysql.YEAR(display_width=4), nullable=False),
    sa.Column('number_frame', mysql.VARCHAR(length=50), nullable=False),
    sa.ForeignKeyConstraint(['id_client'], ['clients.id_client'], name='fk_vehicles_clients'),
    sa.PrimaryKeyConstraint('id_vehicle'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('repair_details',
    sa.Column('id_detail', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('id_order', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('description', mysql.TEXT(), nullable=False),
    sa.Column('id_replacement', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('amount', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('unit_price', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('subtotal', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['id_order'], ['repair_orders.id_order'], name='fk_repair_details_order', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_order'], ['repair_orders.id_order'], name='fk_reparation_detail_order'),
    sa.ForeignKeyConstraint(['id_replacement'], ['spare_parts_inventory.id_replacement'], name='fk_repair_details_replacement', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_detail'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('clients',
    sa.Column('id_client', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('id_user', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('phone', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('adress', mysql.TEXT(), nullable=False),
    sa.Column('register_date', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['users.id_user'], name='fk_clients_user', onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id_client'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('clients', schema=None) as batch_op:
        batch_op.create_index('email', ['email'], unique=True)

    op.create_table('appoiments',
    sa.Column('id_appoiment', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('id_client', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('id_vehicle', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('appoiment_date', mysql.DATETIME(), nullable=False),
    sa.Column('state', mysql.ENUM('Pendiente', 'Confirmada', 'Cancelada', 'Realizada'), nullable=False),
    sa.Column('notes', mysql.TEXT(), nullable=False),
    sa.ForeignKeyConstraint(['id_client'], ['clients.id_client'], name='fk_appoiments_client'),
    sa.ForeignKeyConstraint(['id_vehicle'], ['vehicles.id_vehicle'], name='fk_appoiments_vehicle'),
    sa.PrimaryKeyConstraint('id_appoiment'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('session_tokens',
    sa.Column('id_token', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('id_user', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('token', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('creation_date', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=False),
    sa.Column('expiration_date', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['users.id_user'], name='fk_session_tokens_users'),
    sa.ForeignKeyConstraint(['id_user'], ['users.id_user'], name='fk_tokens_user', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_token'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('advertisements',
    sa.Column('id_advertisement', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('description', mysql.TEXT(), nullable=False),
    sa.Column('image_path', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('contact', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('publication_date', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=False),
    sa.Column('asset', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id_advertisement'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('spare_parts_inventory',
    sa.Column('id_replacement', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('description', mysql.TEXT(), nullable=False),
    sa.Column('price', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.PrimaryKeyConstraint('id_replacement'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('payments',
    sa.Column('id_payment', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('id_invoice', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('id_client', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('amount', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('payment_method', mysql.ENUM('Efectivo', 'Tarjeta', 'Transferencia', 'Otros'), nullable=False),
    sa.Column('payment_date', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=False),
    sa.Column('state', mysql.ENUM('Pendiente', 'Cobrado'), nullable=False),
    sa.ForeignKeyConstraint(['id_client'], ['clients.id_client'], name='fk_payments_client'),
    sa.ForeignKeyConstraint(['id_invoice'], ['invoices.id_invoice'], name='fk_payments_invoice'),
    sa.PrimaryKeyConstraint('id_payment'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('employees',
    sa.Column('id_employee', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('id_user', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('phone', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('adress', mysql.TEXT(), nullable=False),
    sa.Column('post', mysql.ENUM('Administrador', 'Mecánico'), nullable=False),
    sa.Column('salary', mysql.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('date_start', mysql.DATETIME(), server_default=sa.text('current_timestamp()'), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['users.id_user'], name='fk_employees_id_users', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_employee'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.create_index('id_user', ['id_user'], unique=True)
        batch_op.create_index('email', ['email'], unique=True)

    op.create_table('users',
    sa.Column('id_user', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('user_type', mysql.ENUM('Administrador', 'Mecánico', 'Cliente', 'Visitante'), nullable=False),
    sa.Column('registration_date', mysql.TIMESTAMP(), server_default=sa.text('current_timestamp()'), nullable=False),
    sa.PrimaryKeyConstraint('id_user'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('email', ['email'], unique=True)

    # ### end Alembic commands ###
