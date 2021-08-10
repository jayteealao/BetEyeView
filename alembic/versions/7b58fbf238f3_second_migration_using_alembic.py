"""second migration using alembic

Revision ID: 7b58fbf238f3
Revises: 6594b62392b4
Create Date: 2021-08-10 13:15:45.439327

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7b58fbf238f3'
down_revision = '6594b62392b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('betking_book', schema='test')
    op.drop_table('nairabet_book', schema='test')
    op.drop_table('bet9ja_book', schema='test')
    op.drop_table('book', schema='test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('test.book_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('match', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('match_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('league', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('bet9ja_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('betking_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('nairabet_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='book_pkey'),
    sa.UniqueConstraint('bet9ja_id', name='book_bet9ja_id_key'),
    sa.UniqueConstraint('betking_id', name='book_betking_id_key'),
    sa.UniqueConstraint('nairabet_id', name='book_nairabet_id_key'),
    schema='test',
    postgresql_ignore_search_path=False
    )
    op.create_table('bet9ja_book',
    sa.Column('match_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('book_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('continent_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['test.book.id'], name='bet9ja_book_book_id_fkey'),
    sa.ForeignKeyConstraint(['match_id'], ['test.book.bet9ja_id'], name='bet9ja_book_match_id_fkey'),
    sa.PrimaryKeyConstraint('match_id', name='bet9ja_book_pkey'),
    schema='test'
    )
    op.create_table('nairabet_book',
    sa.Column('match_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('book_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('continent_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['test.book.id'], name='nairabet_book_book_id_fkey'),
    sa.ForeignKeyConstraint(['match_id'], ['test.book.nairabet_id'], name='nairabet_book_match_id_fkey'),
    sa.PrimaryKeyConstraint('match_id', name='nairabet_book_pkey'),
    schema='test'
    )
    op.create_table('betking_book',
    sa.Column('match_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('book_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('continent_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['test.book.id'], name='betking_book_book_id_fkey'),
    sa.ForeignKeyConstraint(['match_id'], ['test.book.betking_id'], name='betking_book_match_id_fkey'),
    sa.PrimaryKeyConstraint('match_id', name='betking_book_pkey'),
    schema='test'
    )
    # ### end Alembic commands ###