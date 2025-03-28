from flask import jsonify, request
from models import User, Policy, db

def init_routes(app):
    @app.route('/api/user/balance', methods=['GET'])
    def get_balance():
        user_id = request.args.get('user_id')
        user = User.query.get(user_id)
        if user:
            return jsonify({'balance': user.balance})
        return jsonify({'error': 'User not found'}), 404

    @app.route('/api/vote', methods=['POST'])
    def vote_on_policy():
        data = request.json
        policy_id = data['policy_id']
        vote = data['vote']
        policy = Policy.query.get(policy_id)
        if policy:
            # Update votes based on the user's vote
            if vote == 'for':
                policy.votes_for += 1
            else:
                policy.votes_against += 1
            db.session.commit()
            return jsonify({'message': 'Vote registered'})
        return jsonify({'error': 'Policy not found'}), 404
