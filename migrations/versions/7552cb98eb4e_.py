"""empty message

Revision ID: 7552cb98eb4e
Revises: 2cf6e68f7ddc
Create Date: 2024-10-17 06:09:22.713181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7552cb98eb4e'
down_revision = '2cf6e68f7ddc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritecharacters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('character_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'characters', ['character_id'], ['id'])

    with op.batch_alter_table('favoriteplanets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planet_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'planets', ['planet_id'], ['id'])

    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fcharacter_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('fcvehicle_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('fplanet_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'favoriteplanets', ['fplanet_id'], ['id'])
        batch_op.create_foreign_key(None, 'favoritecharacters', ['fcharacter_id'], ['id'])
        batch_op.create_foreign_key(None, 'favoritevehicles', ['fcvehicle_id'], ['id'])

    with op.batch_alter_table('favoritevehicles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vehicle_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'vehicles', ['vehicle_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritevehicles', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('vehicle_id')

    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('fplanet_id')
        batch_op.drop_column('fcvehicle_id')
        batch_op.drop_column('fcharacter_id')

    with op.batch_alter_table('favoriteplanets', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('planet_id')

    with op.batch_alter_table('favoritecharacters', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('character_id')

    # ### end Alembic commands ###
